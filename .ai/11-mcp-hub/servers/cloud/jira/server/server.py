import os
import json
import requests
from typing import Dict, Any, Optional, List
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("jira-rest-fallback")

def get_jira_client():
    """Helper to get a configured requests session for Jira REST API"""
    url = os.environ.get("JIRA_REST_URL")
    user = os.environ.get("JIRA_REST_USER")
    token = os.environ.get("JIRA_REST_API_TOKEN")

    if not url or not user or not token:
        raise ValueError("Missing Jira environment variables (JIRA_REST_URL, JIRA_REST_USER, JIRA_REST_API_TOKEN)")

    session = requests.Session()
    session.auth = (user, token)
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json"
    })
    
    # Ensure URL doesn't have trailing slash for consistency
    url = url.rstrip('/')
    return session, url

# ----------------------------------------------------------------------------
# READ OPERATIONS (auto_fallback: true)
# ----------------------------------------------------------------------------

@mcp.tool()
def get_issue(key: str) -> str:
    """Get a Jira issue by its key."""
    try:
        session, base_url = get_jira_client()
        response = session.get(f"{base_url}/rest/api/3/issue/{key}")
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def search_issues(jql: str) -> str:
    """Search Jira issues using JQL."""
    try:
        session, base_url = get_jira_client()
        response = session.get(f"{base_url}/rest/api/3/search", params={"jql": jql})
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_projects() -> str:
    """List all Jira projects visible to the user."""
    try:
        session, base_url = get_jira_client()
        response = session.get(f"{base_url}/rest/api/3/project")
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_issue_types(project: str) -> str:
    """Get all issue types available for a specific project."""
    try:
        session, base_url = get_jira_client()
        response = session.get(f"{base_url}/rest/api/3/project/{project}")
        response.raise_for_status()
        project_data = response.json()
        return json.dumps(project_data.get("issueTypes", []), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_field_metadata(project: str, issue_type: str) -> str:
    """Get metadata for fields required to create an issue of a specific type in a project."""
    try:
        session, base_url = get_jira_client()
        response = session.get(
            f"{base_url}/rest/api/3/issue/createmeta",
            params={
                "projectKeys": project,
                "issuetypeNames": issue_type,
                "expand": "projects.issuetypes.fields"
            }
        )
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def lookup_user(query: str) -> str:
    """Find a Jira user by name or email."""
    try:
        session, base_url = get_jira_client()
        response = session.get(f"{base_url}/rest/api/3/user/search", params={"query": query})
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

# ----------------------------------------------------------------------------
# WRITE OPERATIONS (Require idempotency_key + human_confirmation via Gateway)
# ----------------------------------------------------------------------------

@mcp.tool()
def create_issue(project: str, issue_type: str, fields: str, idempotency_key: str) -> str:
    """Create a new Jira issue."""
    try:
        session, base_url = get_jira_client()
        
        # NOTE: Gateway should handle idempotency checks. 
        # Here we just execute the write operation.
        
        payload = {
            "fields": {
                "project": {"key": project},
                "issuetype": {"name": issue_type}
            }
        }
        
        # Merge additional fields
        additional_fields = json.loads(fields)
        payload["fields"].update(additional_fields)
        
        response = session.post(f"{base_url}/rest/api/3/issue", json=payload)
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def edit_issue(key: str, fields: str, idempotency_key: str) -> str:
    """Edit an existing Jira issue."""
    try:
        session, base_url = get_jira_client()
        payload = {"fields": json.loads(fields)}
        
        response = session.put(f"{base_url}/rest/api/3/issue/{key}", json=payload)
        response.raise_for_status()
        return f"Issue {key} updated successfully."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def transition_issue(key: str, transition_id: str, idempotency_key: str) -> str:
    """Transition a Jira issue to a new status."""
    try:
        session, base_url = get_jira_client()
        payload = {"transition": {"id": transition_id}}
        
        response = session.post(f"{base_url}/rest/api/3/issue/{key}/transitions", json=payload)
        response.raise_for_status()
        return f"Issue {key} transitioned successfully."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def add_comment(key: str, body: str, idempotency_key: str) -> str:
    """Add a comment to a Jira issue (Atlassian Document Format)."""
    try:
        session, base_url = get_jira_client()
        
        # Construct ADF simple text structure
        payload = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": body
                            }
                        ]
                    }
                ]
            }
        }
        
        response = session.post(f"{base_url}/rest/api/3/issue/{key}/comment", json=payload)
        response.raise_for_status()
        return f"Comment added to {key} successfully."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def add_worklog(key: str, time_spent: str, idempotency_key: str) -> str:
    """Add a worklog to a Jira issue (e.g. time_spent = '1h 30m')."""
    try:
        session, base_url = get_jira_client()
        payload = {"timeSpent": time_spent}
        
        response = session.post(f"{base_url}/rest/api/3/issue/{key}/worklog", json=payload)
        response.raise_for_status()
        return f"Worklog added to {key} successfully."
    except Exception as e:
        return f"Error: {str(e)}"

# ----------------------------------------------------------------------------
# UNSUPPORTED / EXCLUDED OPERATIONS
# ----------------------------------------------------------------------------

@mcp.tool()
def set_backlog_rank(key: str, rank: str) -> str:
    """Change the backlog rank of an issue."""
    return "Unsupported by active provider"

# delete_issue is explicitly NOT implemented for safety.

if __name__ == "__main__":
    mcp.run()
