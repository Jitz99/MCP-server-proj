🧮 Calculator MCP Server (Python)

This repository demonstrates two ways of exposing tools using MCP (Model Context Protocol) in Python:

Native MCP Server using fastmcp

FastAPI-based HTTP API exposed as MCP tools using fastapi-mcp

Both implementations expose a simple Calculator with arithmetic operations.

📁 Project Structure
.
├── mcp_calculator.py        # Native MCP (STDIO) server
├── fastapi_calculator.py   # FastAPI + MCP bridge
└── README.md

1️⃣ Native MCP Server (fastmcp)
📄 mcp_calculator.py

This implementation uses fastmcp.FastMCP to expose calculator functions directly as MCP tools over STDIO.

🔹 Exposed Tools
Tool Name	Description
multiply	Multiply two numbers
add	Add two numbers
subtract	Subtract two numbers
divide	Divide two numbers (with zero check)
🔹 Example Tool Definition
@mcp.tool()
def multiply(a: float, b: float) -> float:
    return a * b

🔹 Run the MCP Server
python mcp_calculator.py


This starts a STDIO-based MCP server, compatible with:

Claude Desktop

Cursor

MCP-compatible agents

✅ When to use this approach

Claude / Cursor integrations

Local agent tools

Lightweight MCP servers

No HTTP required

2️⃣ FastAPI + MCP Bridge (fastapi-mcp)
📄 fastapi_calculator.py

This implementation:

Creates a FastAPI REST API

Automatically exposes endpoints as MCP tools using FastApiMCP

🔹 REST Endpoints
HTTP Endpoint	Method	Description
/multiply	POST	Multiply two numbers
/Add	POST	Add two numbers
/substract	POST	Subtract two numbers
/divide	POST	Divide two numbers
🔹 MCP Integration
mcp = FastApiMCP(app, name="Calculator MCP")
mcp.mount()


This converts all FastAPI routes into MCP-compatible tools.

🔹 Run the FastAPI MCP Server
python fastapi_calculator.py


Server starts at:

http://localhost:8002


Swagger UI:

http://localhost:8002/docs

✅ When to use this approach

Cloud-deployable MCP servers

Multi-language clients (.NET, Python, JS)

Existing FastAPI applications

Microservices + MCP tools

🧠 MCP Comparison
Feature	fastmcp	fastapi-mcp
Transport	STDIO	HTTP
Cloud friendly	❌	✅
Claude / Cursor	✅	⚠️
REST support	❌	✅
Production APIs	❌	✅