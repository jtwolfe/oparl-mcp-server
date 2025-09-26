# Server API-Referenz

API-Referenz für den OParl MCP Server.

## OParlMCPServer

Hauptserver-Klasse für den OParl MCP Server.

### Konstruktor

```python
OParlMCPServer(config: Optional[OParlConfig] = None)
```

**Parameter:**
- `config` (Optional[OParlConfig]): Konfigurationsobjekt. Wenn None, wird Standardkonfiguration verwendet.

### Methoden

#### `run()`
Startet den MCP-Server.

```python
server.run()
```

#### `get_server_info() -> dict`
Ruft Informationen über den MCP-Server ab.

**Rückgabe:**
- `dict`: Serverinformationen einschließlich Name, Version, Basis-URL und Funktionen.

**Beispiel:**
```python
info = server.get_server_info()
print(f"Server: {info['name']}")
print(f"Version: {info['version']}")
print(f"Funktionen: {info['features']}")
```

## OParlConfig

Konfigurationsklasse für OParl MCP Server.

### Konstruktor

```python
OParlConfig(
    base_url: str = "https://api.oparl.org",
    api_key: Optional[str] = None,
    timeout: float = 30.0,
    server_name: str = "OParl MCP Server",
    server_version: str = "0.1.0",
    log_level: str = "INFO"
)
```

**Parameter:**
- `base_url` (str): Basis-URL der OParl API
- `api_key` (Optional[str]): API-Schlüssel für Authentifizierung
- `timeout` (float): Anforderungs-Timeout in Sekunden
- `server_name` (str): Servername
- `server_version` (str): Serverversion
- `log_level` (str): Protokollierungsstufe
