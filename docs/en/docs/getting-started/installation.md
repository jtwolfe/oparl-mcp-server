# Installation

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Quick Installation

### Using pip

```bash
pip install oparl-mcp-server
```

### From source

```bash
git clone https://github.com/oparl-mcp-team/oparl-mcp-server.git
cd oparl-mcp-server
pip install -e .
```

## Docker Installation

### Using Docker Hub

```bash
docker pull oparl-mcp-team/oparl-mcp-server:latest
```

### Using GitHub Container Registry

```bash
docker pull ghcr.io/oparl-mcp-team/oparl-mcp-server:latest
```

## Development Installation

For development, install additional dependencies:

```bash
git clone https://github.com/oparl-mcp-team/oparl-mcp-server.git
cd oparl-mcp-server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

## Verification

Test your installation:

```bash
python -c "from oparl_mcp import OParlMCPServer; print('Installation successful!')"
```

Or run the test script:

```bash
python test_setup.py
```
