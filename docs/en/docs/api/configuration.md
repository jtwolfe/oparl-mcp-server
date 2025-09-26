# Configuration API Reference

Configuration options for OParl MCP Server.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPARL_BASE_URL` | `https://api.oparl.org` | Base URL of the OParl API |
| `OPARL_API_KEY` | `None` | API key for authentication |
| `OPARL_TIMEOUT` | `30.0` | Request timeout in seconds |
| `OPARL_LOG_LEVEL` | `INFO` | Logging level |
| `OPARL_SERVER_NAME` | `OParl MCP Server` | Server name |
| `OPARL_SERVER_VERSION` | `0.1.0` | Server version |

## Configuration File

Create a `.env` file in your project root:

```env
OPARL_BASE_URL=https://oparl.muenchen.de
OPARL_API_KEY=your-munich-api-key
OPARL_TIMEOUT=45.0
OPARL_LOG_LEVEL=INFO
OPARL_SERVER_NAME=Munich OParl Server
```

## Programmatic Configuration

```python
from oparl_mcp import OParlConfig

config = OParlConfig(
    base_url="https://custom.oparl.api.com",
    api_key="your-api-key",
    timeout=60.0,
    server_name="Custom OParl Server",
    log_level="DEBUG"
)
```

## Logging Configuration

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Docker Configuration

```yaml
version: '3.8'
services:
  oparl-mcp-server:
    image: oparl-mcp-server:latest
    environment:
      - OPARL_BASE_URL=https://oparl.muenchen.de
      - OPARL_API_KEY=your-key
      - OPARL_TIMEOUT=60.0
      - OPARL_LOG_LEVEL=INFO
```
