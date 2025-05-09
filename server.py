import asyncio
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import mcp.types as types
import sqlite3
from loguru import logger



mcp = FastMCP("magic_number")

@mcp.tool(name="magic",description="Gives a magic number")
async def get_magic():
    return "your magic number is 2"



@mcp.prompt()
def example_prompt(code: str) -> str:
    return f"Please review this code:\n\n{code}"


if __name__ == "__main__":
    print("Magic MCP Server starting...")
    # Run the server, listening via standard input/output
    mcp.run(transport='stdio')
    print("Magic MCP Server stopped.")
