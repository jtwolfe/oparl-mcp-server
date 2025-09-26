# Konfiguration

OParl MCP Server für Ihre spezifischen Bedürfnisse konfigurieren.

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|----------|----------|--------------|
| `OPARL_BASE_URL` | `https://api.oparl.org` | Basis-URL der OParl API |
| `OPARL_API_KEY` | `None` | API-Schlüssel für Authentifizierung |
| `OPARL_TIMEOUT` | `30.0` | Anforderungs-Timeout in Sekunden |
| `OPARL_LOG_LEVEL` | `INFO` | Protokollierungsstufe |
| `OPARL_SERVER_NAME` | `OParl MCP Server` | Servername |
| `OPARL_SERVER_VERSION` | `0.1.0` | Serverversion |

## Programmatische Konfiguration

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

## Konfigurationsdatei

Erstellen Sie eine `.env`-Datei im Projektverzeichnis:

```env
OPARL_BASE_URL=https://oparl.muenchen.de
OPARL_API_KEY=your-munich-api-key
OPARL_TIMEOUT=45.0
OPARL_LOG_LEVEL=INFO
```

## Verschiedene OParl-Implementierungen

Der Server unterstützt verschiedene OParl-Implementierungen:

- **Generische OParl API**: `https://api.oparl.org`
- **Münchner Stadtrat**: `https://oparl.muenchen.de`
- **Kölner Stadtrat**: `https://oparl.koeln.de`
- **Hamburger Bürgerschaft**: `https://oparl.hamburg.de`

Jede Implementierung kann unterschiedliche haben:
- Authentifizierungsanforderungen
- Verfügbare Daten
- API-Endpunkte
- Rate-Limits
