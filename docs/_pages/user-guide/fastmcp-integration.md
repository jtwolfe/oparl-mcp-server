---
layout: page
title: "FastMCP Integration"
description: "How FastMCP is used to create MCP tools from OParl API"
permalink: /user-guide/fastmcp-integration/
---

<div align="center">

# FastMCP Integration

<img src="../../assets/images/fastmcp-logo.png" alt="FastMCP Logo" width="200" height="80">

**This guide explains how FastMCP is used to create Model Context Protocol (MCP) tools and resources from the OParl API specification**

</div>

## What is FastMCP?

FastMCP is a Python framework that automatically generates MCP servers from OpenAPI specifications. It provides:

- **Automatic API mapping** from OpenAPI to MCP components
- **Type-safe client generation** for API calls
- **Flexible route mapping** for custom behavior
- **Built-in authentication** support
- **Async/await support** for high performance

## How FastMCP Works with OParl

The OParl MCP Server uses FastMCP to transform the OParl API into MCP-compatible tools and resources:

1. **OpenAPI Specification** → FastMCP reads the `oparl_openapi.json`
2. **Route Mapping** → Custom mapping rules define MCP component types
3. **MCP Server** → FastMCP generates the MCP server automatically
4. **AI Integration** → AI models can use the server via MCP protocol

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AI Model      │    │   MCP Client    │    │   MCP Server    │
│                 │◄──►│                 │◄──►│   (FastMCP)     │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                               ┌─────────────────┐
                                               │   OParl API     │
                                               │   (HTTP/REST)   │
                                               │                 │
                                               └─────────────────┘
```

## Route Mapping Configuration

The server uses custom route mappings to define how OParl API endpoints become MCP components:

### Resource Templates
Individual OParl objects (e.g., specific meetings, people, papers) become MCP Resource Templates:

```python
RouteMap(
    methods=["GET"],
    pattern=r".*\{.*\}.*",  # URLs with parameters like /meeting/{id}
    mcp_type=MCPType.RESOURCE_TEMPLATE,
    mcp_tags={"oparl", "data", "individual", "parameterized"},
)
```

**Examples:**
- `GET /meeting/123` → Resource Template for specific meeting
- `GET /person/456` → Resource Template for specific person
- `GET /paper/789` → Resource Template for specific paper

### Resources
Collection endpoints (e.g., list all meetings, all people) become MCP Resources:

```python
RouteMap(
    methods=["GET"],
    pattern=r".*",  # All other GET endpoints
    mcp_type=MCPType.RESOURCE,
    mcp_tags={"oparl", "data", "collection", "read-only"},
)
```

**Examples:**
- `GET /meeting` → Resource for meeting list
- `GET /person` → Resource for person list
- `GET /paper` → Resource for paper list

### Tools
Write operations (if any) become MCP Tools:

```python
RouteMap(
    methods=["POST", "PUT", "DELETE"],
    pattern=r".*",
    mcp_type=MCPType.TOOL,
    mcp_tags={"oparl", "action", "write"},
)
```

**Note:** Most OParl implementations are read-only, so tools are rarely used.

### Exclusions
Admin or internal endpoints are excluded from MCP exposure:

```python
RouteMap(pattern=r".*/admin/.*", mcp_type=MCPType.EXCLUDE),
RouteMap(pattern=r".*/internal/.*", mcp_type=MCPType.EXCLUDE),
```

## MCP Component Types

### 1. Resources
Resources provide access to OParl data collections:

**System Resource:**
- **Name**: `oparl_system`
- **Description**: "Access to OParl system information"
- **Tags**: `["oparl", "system", "metadata"]`

**Body Resource:**
- **Name**: `oparl_bodies`
- **Description**: "List of parliamentary bodies"
- **Tags**: `["oparl", "bodies", "parliamentary"]`

**Meeting Resource:**
- **Name**: `oparl_meetings`
- **Description**: "List of parliamentary meetings"
- **Tags**: `["oparl", "meetings", "sessions"]`

### 2. Resource Templates
Resource Templates provide access to specific OParl objects:

**Meeting Template:**
- **Name**: `oparl_meeting_{id}`
- **Description**: "Access to specific meeting details"
- **Parameters**: `id` (meeting identifier)
- **Tags**: `["oparl", "meeting", "individual"]`

**Person Template:**
- **Name**: `oparl_person_{id}`
- **Description**: "Access to specific person details"
- **Parameters**: `id` (person identifier)
- **Tags**: `["oparl", "person", "individual"]`

### 3. Tools
Tools provide actions on OParl data:

**Search Tool:**
- **Name**: `oparl_search`
- **Description**: "Search across OParl data"
- **Parameters**: `query`, `type`, `limit`
- **Tags**: `["oparl", "search", "query"]`

## Authentication Integration

FastMCP handles authentication through the HTTP client:

```python
def _create_http_client(self) -> httpx.AsyncClient:
    """Create HTTP client for OParl API."""
    headers = {}

    # Add authentication if API key is provided
    if self.config.api_key:
        headers["Authorization"] = f"Bearer {self.config.api_key}"

    return httpx.AsyncClient(
        base_url=self.config.base_url,
        headers=headers,
        timeout=self.config.timeout
    )
```

**Supported Authentication Methods:**
- **API Key**: Bearer token authentication
- **No Auth**: Public OParl implementations
- **Custom Headers**: Additional authentication headers

## Error Handling

FastMCP automatically handles HTTP errors and converts them to MCP-compatible responses:

```python
# HTTP 404 → MCP error response
{
    "error": {
        "code": "NOT_FOUND",
        "message": "Resource not found",
        "details": "Meeting with ID 123 not found"
    }
}

# HTTP 500 → MCP error response
{
    "error": {
        "code": "INTERNAL_ERROR",
        "message": "Internal server error",
        "details": "Unable to connect to OParl API"
    }
}
```

## Performance Optimization

FastMCP provides several performance optimizations:

### 1. Connection Pooling
```python
# Reuses HTTP connections for multiple requests
client = httpx.AsyncClient(
    limits=httpx.Limits(max_keepalive_connections=20)
)
```

### 2. Caching
```python
# FastMCP can cache responses based on headers
cache_control = "max-age=3600"  # Cache for 1 hour
```

### 3. Async Operations
```python
# All operations are async for better performance
async def get_meeting(meeting_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"/meeting/{meeting_id}")
        return response.json()
```

## Customization Options

### 1. Custom Route Mappings
You can add custom route mappings for specific behavior:

```python
custom_routes = [
    RouteMap(
        methods=["GET"],
        pattern=r"/meeting/upcoming",
        mcp_type=MCPType.RESOURCE,
        mcp_tags={"oparl", "meetings", "upcoming"},
    )
]
```

### 2. Custom Tags
Add custom tags for better organization:

```python
tags = {
    "oparl": "OParl API integration",
    "parliamentary-data": "Parliamentary information",
    "government": "Government data access",
    "munich": "Munich-specific data",
}
```

### 3. Custom Headers
Add custom headers for specific implementations:

```python
headers = {
    "User-Agent": "OParl-MCP-Server/1.0",
    "Accept": "application/json",
    "X-API-Version": "1.1",
}
```

## Integration Examples

### Basic MCP Client Usage

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    async with stdio_client(StdioServerParameters(
        command="python",
        args=["-m", "oparl_mcp.server"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            # List all meetings
            meetings = await session.list_resources()
            print(f"Found {len(meetings)} resources")

            # Get specific meeting
            meeting = await session.read_resource(
                "oparl_meeting_123"
            )
            print(f"Meeting: {meeting['name']}")
```

### Advanced Usage with Parameters

```python
async def search_meetings(session, query: str):
    """Search for meetings using MCP tools."""
    result = await session.call_tool(
        "oparl_search",
        arguments={
            "query": query,
            "type": "meeting",
            "limit": 10
        }
    )
    return result
```

## Troubleshooting

### Common Issues

1. **Connection Errors**
   - Check OParl API availability
   - Verify base URL configuration
   - Check network connectivity

2. **Authentication Errors**
   - Verify API key validity
   - Check authentication method
   - Ensure proper header format

3. **Rate Limiting**
   - Implement request throttling
   - Use caching for repeated requests
   - Monitor API usage limits

### Debug Mode

Enable debug logging to troubleshoot issues:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# FastMCP will log detailed information about:
# - HTTP requests and responses
# - Route mapping decisions
# - Error handling
# - Performance metrics
```

## Next Steps

- [MCP Components]({{ '/user-guide/mcp-components' | relative_url }}) - Detailed MCP component reference
- [Examples]({{ '/user-guide/examples' | relative_url }}) - Practical usage examples
- [API Reference]({{ '/api/server' | relative_url }}) - Complete API documentation
