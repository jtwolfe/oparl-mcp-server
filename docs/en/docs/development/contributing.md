# Contributing

Thank you for your interest in contributing to OParl MCP Server!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment
4. Install development dependencies

```bash
git clone https://github.com/your-username/oparl-mcp-server.git
cd oparl-mcp-server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
```

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- Docker (optional)

### Code Style
We use Black for code formatting and isort for import sorting:

```bash
black src/ tests/ examples/
isort src/ tests/ examples/
```

### Type Checking
We use mypy for type checking:

```bash
mypy src/
```

### Testing
Run the test suite:

```bash
pytest tests/
```

## Pull Request Process

1. Create a feature branch from `dev`
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Update documentation if needed
6. Submit a pull request

## Code of Conduct

Please be respectful and constructive in all interactions.

## Questions?

Feel free to open an issue for questions or discussions.
