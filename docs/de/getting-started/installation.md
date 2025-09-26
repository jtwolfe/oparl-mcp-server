# Installation

## Voraussetzungen

- Python 3.8 oder höher
- pip (Python-Paketmanager)

## Schnelle Installation

### Mit pip

```bash
pip install oparl-mcp-server
```

### Aus dem Quellcode

```bash
git clone https://github.com/oparl-mcp-team/oparl-mcp-server.git
cd oparl-mcp-server
pip install -e .
```

## Docker-Installation

### Mit Docker Hub

```bash
docker pull oparl-mcp-team/oparl-mcp-server:latest
```

### Mit GitHub Container Registry

```bash
docker pull ghcr.io/oparl-mcp-team/oparl-mcp-server:latest
```

## Entwicklungs-Installation

Für die Entwicklung zusätzliche Abhängigkeiten installieren:

```bash
git clone https://github.com/oparl-mcp-team/oparl-mcp-server.git
cd oparl-mcp-server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

## Überprüfung

Testen Sie Ihre Installation:

```bash
python -c "from oparl_mcp import OParlMCPServer; print('Installation erfolgreich!')"
```

Oder führen Sie das Test-Skript aus:

```bash
python test_setup.py
```
