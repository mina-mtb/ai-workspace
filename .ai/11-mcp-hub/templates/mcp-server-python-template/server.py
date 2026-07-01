from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("TemplateServer")

@mcp.tool()
def sample_tool(name: str) -> str:
    """A sample tool that greets the user."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()
