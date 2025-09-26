# Configuration

Configure OParl MCP Server for your specific needs.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPARL_BASE_URL` | `https://api.oparl.org` | Base URL of the OParl API |
| `OPARL_API_KEY` | `None` | API key for authentication |
| `OPARL_TIMEOUT` | `30.0` | Request timeout in seconds |
| `OPARL_LOG_LEVEL` | `INFO` | Logging level |
| `OPARL_SERVER_NAME` | `OParl MCP Server` | Server name |
| `OPARL_SERVER_VERSION` | `0.1.0` | Server version |

## Programmatic Configuration

```python
from oparl_mcp import OParlConfig, OParlMCPServer

config = OParlConfig(
    base_url="https://custom.oparl.api.com",
    api_key="your-api-key",
    timeout=60.0,
    server_name="Custom OParl Server",
    log_level="DEBUG"
)

server = OParlMCPServer(config)
server.run()
```

## Configuration File

Create a `.env` file in your project root:

```env
OPARL_BASE_URL=https://oparl.muenchen.de
OPARL_API_KEY=your-munich-api-key
OPARL_TIMEOUT=45.0
OPARL_LOG_LEVEL=INFO
```

## Multiple OParl Implementations

The server supports various OParl implementations:

- **Generic OParl API**: `https://api.oparl.org`
- **Munich City Council**: `https://oparl.muenchen.de`
- **Cologne City Council**: `https://oparl.koeln.de`
- **Hamburg Parliament**: `https://oparl.hamburg.de`

Each implementation may have different:
- Authentication requirements
- Available data
- API endpoints
- Rate limits
