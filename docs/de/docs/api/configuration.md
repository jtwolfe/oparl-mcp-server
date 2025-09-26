# Konfiguration API-Referenz

Konfigurationsoptionen für OParl MCP Server.

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|----------|----------|--------------|
| `OPARL_BASE_URL` | `https://api.oparl.org` | Basis-URL der OParl API |
| `OPARL_API_KEY` | `None` | API-Schlüssel für Authentifizierung |
| `OPARL_TIMEOUT` | `30.0` | Anforderungs-Timeout in Sekunden |
| `OPARL_LOG_LEVEL` | `INFO` | Protokollierungsstufe |
| `OPARL_SERVER_NAME` | `OParl MCP Server` | Servername |
| `OPARL_SERVER_VERSION` | `0.1.0` | Serverversion |

## Konfigurationsdatei

Erstellen Sie eine `.env`-Datei im Projektverzeichnis:

```env
OPARL_BASE_URL=https://oparl.muenchen.de
OPARL_API_KEY=your-munich-api-key
OPARL_TIMEOUT=45.0
OPARL_LOG_LEVEL=INFO
OPARL_SERVER_NAME=Munich OParl Server
```

## Programmatische Konfiguration

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
