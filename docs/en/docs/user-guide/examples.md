# Examples

Practical examples of using OParl MCP Server.

## Basic Server Setup

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Default configuration
config = OParlConfig()
server = OParlMCPServer(config)
server.run()
```

## Custom Configuration

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Custom configuration
config = OParlConfig(
    base_url="https://oparl.muenchen.de",
    api_key="your-api-key",
    timeout=60.0,
    server_name="Munich OParl Server"
)

server = OParlMCPServer(config)
server.run()
```

## Docker Usage

```bash
# Run with default configuration
docker run -p 8000:8000 oparl-mcp-server:latest

# Run with custom configuration
docker run -p 8000:8000 \
  -e OPARL_BASE_URL=https://oparl.muenchen.de \
  -e OPARL_API_KEY=your-key \
  oparl-mcp-server:latest
```

## Docker Compose

```yaml
version: '3.8'
services:
  oparl-mcp-server:
    image: oparl-mcp-server:latest
    ports:
      - "8000:8000"
    environment:
      - OPARL_BASE_URL=https://oparl.muenchen.de
      - OPARL_API_KEY=your-key
      - OPARL_TIMEOUT=60.0
```

## MCP Client Usage

```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000") as client:
        # Get system information
        system = await client.get_resource("system")
        print(f"System: {system['name']}")
        
        # Get list of bodies
        bodies = await client.get_resource("body", {"limit": 5})
        print(f"Found {len(bodies['data'])} bodies")
        
        # Get specific meeting
        meeting = await client.get_resource_template(
            "meeting", 
            {"meetingId": "123"}
        )
        print(f"Meeting: {meeting['name']}")

asyncio.run(main())
```

## Error Handling

```python
from oparl_mcp import OParlMCPServer, OParlConfig
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    config = OParlConfig()
    server = OParlMCPServer(config)
    server.run()
except KeyboardInterrupt:
    print("Server stopped by user")
except Exception as e:
    print(f"Server error: {e}")
    raise
```

## Environment Configuration

```bash
# .env file
OPARL_BASE_URL=https://oparl.muenchen.de
OPARL_API_KEY=your-munich-api-key
OPARL_TIMEOUT=45.0
OPARL_LOG_LEVEL=DEBUG
OPARL_SERVER_NAME=Munich OParl MCP Server
```

## Production Deployment

```bash
# Build Docker image
docker build -f docker/Dockerfile -t oparl-mcp-server .

# Run with production settings
docker run -d \
  --name oparl-mcp-server \
  -p 8000:8000 \
  -e OPARL_BASE_URL=https://api.oparl.org \
  -e OPARL_LOG_LEVEL=INFO \
  --restart unless-stopped \
  oparl-mcp-server:latest
```
