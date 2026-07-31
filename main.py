from fastmcp import FastMCP
import random

# Create MCP server
mcp = FastMCP("Simple MCP Server")


@mcp.tool
def generate_random_integer(min_value: int = 1, max_value: int = 100) -> int:
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    """
    return a + b

@mcp.resource("info://server")
def server_info() -> str:
    """Information about this MCP server."""
    return """
Simple MCP Server

Available Tools:
1. generate_random_integer(min_value, max_value)
   - Returns a random integer between the given range.

2. add_numbers(a, b)
   - Returns the sum of two numbers.

Author: Nilesh
Version: 1.0.0
"""

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)