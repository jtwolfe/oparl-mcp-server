# Schnellstart

In wenigen Minuten mit OParl MCP Server loslegen.

## Installation

```bash
pip install oparl-mcp-server
```

## Grundlegende Verwendung

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Server mit Standardkonfiguration erstellen
config = OParlConfig()
server = OParlMCPServer(config)

# Server starten
server.run()
```

## Docker-Verwendung

```bash
docker run -p 8000:8000 oparl-mcp-server:latest
```

## Konfiguration

Umgebungsvariablen für benutzerdefinierte Konfiguration setzen:

```bash
export OPARL_BASE_URL="https://api.oparl.org"
export OPARL_API_KEY="your-api-key"
export OPARL_TIMEOUT="30.0"
```

## Nächste Schritte

- [Konfigurationsanleitung](configuration.md)
- [Benutzerhandbuch](../user-guide/overview.md)
- [API-Referenz](../api/server.md)
