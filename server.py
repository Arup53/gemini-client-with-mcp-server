from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("magic_number")

@mcp.tool()
async def get_magic():
    return "your magic number is 2"



if __name__ == "__main__":
    print("Magic MCP Server starting...")
    # Run the server, listening via standard input/output
    mcp.run(transport='stdio')
    print("Magic MCP Server stopped.")
