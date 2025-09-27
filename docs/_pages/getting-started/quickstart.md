---
layout: page
title: "Quick Start"
description: "Get up and running with OParl MCP Server in minutes"
permalink: /getting-started/quickstart/
---

# Quick Start

Get up and running with OParl MCP Server in minutes.

## Installation

```bash
pip install oparl-mcp-server
```

## Basic Usage

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Create server with default configuration
config = OParlConfig()
server = OParlMCPServer(config)

# Run the server
server.run()
```

## Docker Usage

```bash
docker run -p 8000:8000 oparl-mcp-server:latest
```

## Configuration

Set environment variables for custom configuration:

```bash
export OPARL_BASE_URL="https://api.oparl.org"
export OPARL_API_KEY="your-api-key"
export OPARL_TIMEOUT="30.0"
```

## Next Steps

- [Configuration Guide]({{ '/getting-started/configuration' | relative_url }})
- [User Guide]({{ '/user-guide/overview' | relative_url }})
- [API Reference]({{ '/api/server' | relative_url }})
