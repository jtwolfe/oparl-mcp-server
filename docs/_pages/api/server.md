---
layout: page
title: "Server API"
description: "OParlMCPServer class reference and configuration"
permalink: /api/server/
---

# Server API

The `OParlMCPServer` class is the main entry point for the OParl MCP Server.

## Class: OParlMCPServer

### Constructor

```python
OParlMCPServer(config: Optional[OParlConfig] = None)
```

Creates a new OParl MCP Server instance.

**Parameters:**
- `config` (Optional[OParlConfig]): Configuration object. If None, uses default configuration.

### Methods

#### `run() -> None`

Runs the MCP server. This method starts the server and begins accepting MCP protocol requests.

**Raises:**
- `RuntimeError`: If the server is not properly initialized

#### `get_server_info() -> dict`

Returns information about the MCP server.

**Returns:**
- `dict`: Server information including name, version, base URL, OParl version, and features

**Example:**
```python
server = OParlMCPServer()
info = server.get_server_info()
print(f"Server: {info['name']}")
print(f"Version: {info['version']}")
print(f"Features: {info['features']}")
```

### Properties

#### `config: OParlConfig`

The configuration object used by the server.

#### `mcp: Optional[FastMCP]`

The underlying FastMCP instance. This is None until the server is initialized.

## Example Usage

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Create custom configuration
config = OParlConfig(
    base_url="https://oparl.muenchen.de",
    api_key="your-api-key",
    timeout=60.0,
    server_name="Munich OParl Server"
)

# Create and run server
server = OParlMCPServer(config)
server.run()
```

## Error Handling

The server handles various error conditions:

- **Configuration Errors**: Invalid configuration values
- **Network Errors**: Connection timeouts and HTTP errors
- **Authentication Errors**: Invalid API keys or tokens
- **OpenAPI Errors**: Missing or invalid OpenAPI specification

## Logging

The server uses Python's standard logging module. Configure logging level via the `log_level` configuration parameter.

```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("oparl_mcp")

# Server will use this logger
server = OParlMCPServer()
```
