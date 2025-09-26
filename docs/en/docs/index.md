# OParl MCP Server

A Model Context Protocol (MCP) server for the OParl API, built with FastMCP. This server provides AI models with structured access to parliamentary information systems through the standardized OParl interface.

## 🚀 Features

- **Complete OParl 1.1 Support**: Access to all standard OParl object types
- **MCP Integration**: Seamless integration with AI models via Model Context Protocol
- **Flexible Configuration**: Support for multiple OParl implementations
- **Authentication**: Bearer token and API key support
- **Docker Ready**: Containerized deployment with Docker and Docker Compose
- **Comprehensive Testing**: Unit tests and integration tests included

## 📋 Supported OParl Objects

- **System**: Root system information
- **Body**: Parliamentary bodies (councils, committees)
- **Organization**: Political parties, groups, and organizations
- **Person**: Elected officials, staff, and participants
- **Meeting**: Scheduled meetings and sessions
- **AgendaItem**: Meeting agenda items and topics
- **Paper**: Documents, resolutions, and reports
- **Consultation**: Public consultations and feedback
- **File**: Attachments and media files
- **Location**: Meeting venues and addresses

## 🛠️ Quick Start

### Installation

```bash
pip install oparl-mcp-server
```

### Basic Usage

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Create server with default configuration
config = OParlConfig()
server = OParlMCPServer(config)

# Run the server
server.run()
```

### Docker Usage

```bash
docker run -p 8000:8000 oparl-mcp-server:latest
```

## 📚 Documentation

- [Installation Guide](getting-started/installation.md)
- [Configuration](getting-started/configuration.md)
- [API Reference](api/server.md)
- [Examples](user-guide/examples.md)

## 🌍 OParl Implementations

This server works with various OParl implementations:

- **Generic OParl API**: `https://api.oparl.org`
- **Munich City Council**: `https://oparl.muenchen.de`
- **Cologne City Council**: `https://oparl.koeln.de`
- **Hamburg Parliament**: `https://oparl.hamburg.de`

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](development/contributing.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](about/license.md) file for details.

---

**Made with ❤️ for open government and AI accessibility**
