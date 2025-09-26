# OParl MCP Server

Ein Model Context Protocol (MCP) Server für die OParl API, entwickelt mit FastMCP. Dieser Server bietet KI-Modellen strukturierten Zugang zu parlamentarischen Informationssystemen über die standardisierte OParl-Schnittstelle.

## 🚀 Funktionen

- **Vollständige OParl 1.1-Unterstützung**: Zugang zu allen standardmäßigen OParl-Objekttypen
- **MCP-Integration**: Nahtlose Integration mit KI-Modellen über das Model Context Protocol
- **Flexible Konfiguration**: Unterstützung für mehrere OParl-Implementierungen
- **Authentifizierung**: Bearer Token und API-Schlüssel-Unterstützung
- **Docker-Bereit**: Containerisierte Bereitstellung mit Docker und Docker Compose
- **Umfassende Tests**: Unit-Tests und Integrationstests enthalten

## 📋 Unterstützte OParl-Objekte

- **System**: Root-Systeminformationen
- **Body**: Parlamentarische Gremien (Räte, Ausschüsse)
- **Organization**: Politische Parteien, Gruppen und Organisationen
- **Person**: Gewählte Amtsträger, Personal und Teilnehmer
- **Meeting**: Geplante Sitzungen und Termine
- **AgendaItem**: Tagesordnungspunkte und Themen
- **Paper**: Dokumente, Beschlüsse und Berichte
- **Consultation**: Öffentliche Konsultationen und Feedback
- **File**: Anhänge und Mediendateien
- **Location**: Sitzungsorte und Adressen

## 🛠️ Schnellstart

### Installation

```bash
pip install oparl-mcp-server
```

### Grundlegende Verwendung

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Server mit Standardkonfiguration erstellen
config = OParlConfig()
server = OParlMCPServer(config)

# Server starten
server.run()
```

### Docker-Verwendung

```bash
docker run -p 8000:8000 oparl-mcp-server:latest
```

## 📚 Dokumentation

- [Installationsanleitung](getting-started/installation.md)
- [Konfiguration](getting-started/configuration.md)
- [API-Referenz](api/server.md)
- [Beispiele](user-guide/examples.md)

## 🌍 OParl-Implementierungen

Dieser Server funktioniert mit verschiedenen OParl-Implementierungen:

- **Generische OParl API**: `https://api.oparl.org`
- **Münchner Stadtrat**: `https://oparl.muenchen.de`
- **Kölner Stadtrat**: `https://oparl.koeln.de`
- **Hamburger Bürgerschaft**: `https://oparl.hamburg.de`

## 🤝 Beitragen

Wir freuen uns über Beiträge! Bitte lesen Sie unsere [Beitragsrichtlinien](development/contributing.md) für Details.

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe [LICENSE](about/license.md) für Details.

---

**Mit ❤️ für offene Regierung und KI-Zugänglichkeit erstellt**
