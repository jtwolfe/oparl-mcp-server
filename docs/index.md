---
layout: default
title: "OParl MCP Server"
description: "Model Context Protocol server for accessing OParl parliamentary data APIs"
---

# OParl MCP Server

A powerful Model Context Protocol (MCP) server that provides seamless access to OParl parliamentary data APIs. This server enables AI assistants and applications to interact with parliamentary information systems using a standardized interface.

## 🚀 Quick Start

Get started with the OParl MCP Server in minutes:

```bash
# Install the package
pip install oparl-mcp-server

# Run the server
python -m oparl_mcp.server
```

## ✨ Features

- **🔌 MCP Integration**: Full Model Context Protocol compliance
- **🏛️ OParl Support**: Access to all OParl 1.1 object types
- **🌐 Multi-Implementation**: Works with various OParl implementations
- **🔐 Authentication**: Support for API key authentication
- **📊 Rich Data**: Parliamentary meetings, documents, organizations, and more
- **🔍 Search**: Advanced search and filtering capabilities
- **🐳 Docker Ready**: Containerized deployment options

## 📚 Documentation

- **[Getting Started]({{ '/getting-started/quickstart' | relative_url }})** - Quick setup and basic usage
- **[User Guide]({{ '/user-guide/overview' | relative_url }})** - Comprehensive usage documentation
- **[API Reference]({{ '/api/server' | relative_url }})** - Complete API documentation
- **[Development]({{ '/development/contributing' | relative_url }})** - Contributing and development guide

## 🏛️ Supported OParl Objects

- **System** - API system information
- **Body** - Parliamentary bodies and institutions
- **Organization** - Political parties and groups
- **Person** - Representatives and officials
- **Meeting** - Parliamentary sessions and events
- **AgendaItem** - Meeting agenda items
- **Paper** - Documents and papers
- **Consultation** - Public consultations
- **File** - Attachments and media
- **Location** - Meeting venues and addresses

## 🌍 OParl Implementations

The server works with various OParl implementations:

- **Generic OParl API** - `https://api.oparl.org`
- **Munich City Council** - `https://oparl.muenchen.de`
- **Cologne City Council** - `https://oparl.koeln.de`
- **Hamburg Parliament** - `https://oparl.hamburg.de`

## 🛠️ Installation

### From PyPI

```bash
pip install oparl-mcp-server
```

### From Source

```bash
git clone https://github.com/jtwolfe/oparl-mcp-server.git
cd oparl-mcp-server
pip install -e .
```

### Docker

```bash
docker run -p 8000:8000 jtwolfe/oparl-mcp-server
```

## 📖 Usage

### Basic Configuration

```python
from oparl_mcp import OParlMCPServer, OParlConfig

# Create configuration
config = OParlConfig(
    base_url="https://api.oparl.org",
    api_key="your-api-key",  # Optional
    timeout=30.0
)

# Create and run server
server = OParlMCPServer(config)
server.run()
```

### Environment Variables

```bash
export OPARL_BASE_URL="https://api.oparl.org"
export OPARL_API_KEY="your-api-key"
export OPARL_TIMEOUT="30.0"
export OPARL_LOG_LEVEL="INFO"
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide]({{ '/development/contributing' | relative_url }}) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE]({{ '/about/license' | relative_url }}) file for details.

## 🙏 Acknowledgments

- [OParl](https://oparl.org/) for the parliamentary data standard
- [FastMCP](https://gofastmcp.com/) for the MCP framework
- The open-source community for inspiration and support

---

**Ready to get started?** Check out our [Quick Start Guide]({{ '/getting-started/quickstart' | relative_url }}) or explore the [API Reference]({{ '/api/server' | relative_url }}).
