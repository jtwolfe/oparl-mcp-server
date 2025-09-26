# Testing

Testing guidelines and practices for OParl MCP Server.

## Running Tests

### Unit Tests
```bash
pytest tests/
```

### With Coverage
```bash
pytest tests/ --cov=oparl_mcp --cov-report=html
```

### Specific Test File
```bash
pytest tests/test_config.py
```

### Verbose Output
```bash
pytest tests/ -v
```

## Test Structure

```
tests/
├── test_config.py      # Configuration tests
├── test_server.py      # Server tests
├── test_auth.py        # Authentication tests
└── test_utils.py       # Utility function tests
```

## Writing Tests

### Test Configuration
```python
import pytest
from oparl_mcp import OParlConfig

def test_default_config():
    config = OParlConfig()
    assert config.base_url == "https://api.oparl.org"
    assert config.timeout == 30.0
```

### Test Server
```python
import pytest
from oparl_mcp import OParlMCPServer, OParlConfig

def test_server_initialization():
    config = OParlConfig()
    server = OParlMCPServer(config)
    assert server is not None
```

### Test with Mocking
```python
from unittest.mock import patch, MagicMock

@patch('oparl_mcp.server.httpx.AsyncClient')
def test_api_call(mock_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": "test"}
    mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
    
    # Test your code here
```

## Continuous Integration

Tests run automatically on:
- Push to any branch
- Pull requests
- Multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12, 3.13)

## Test Coverage

We aim for high test coverage. Current coverage can be viewed by running:

```bash
pytest tests/ --cov=oparl_mcp --cov-report=html
open htmlcov/index.html
```
