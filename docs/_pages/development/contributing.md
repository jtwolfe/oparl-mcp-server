---
layout: page
title: "Contributing"
description: "How to contribute to OParl MCP Server"
permalink: /development/contributing/
---

# Contributing

We welcome contributions to OParl MCP Server! This guide will help you get started.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/oparl-mcp-server.git
   cd oparl-mcp-server
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

## Development Setup

### Pre-commit Hooks

Install pre-commit hooks to ensure code quality:

```bash
pip install pre-commit
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/oparl_mcp

# Run specific test file
pytest tests/test_server.py
```

### Code Quality

The project uses several tools for code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security scanning
- **detect-secrets**: Secret detection

Run all quality checks:

```bash
pre-commit run --all-files
```

## Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards

3. **Write tests** for new functionality

4. **Update documentation** if needed

5. **Run tests and quality checks**:
   ```bash
   pytest
   pre-commit run --all-files
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add your feature description"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** on GitHub

## Coding Standards

### Python Code

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Use meaningful variable and function names

### Documentation

- Update relevant documentation files
- Use clear, concise language
- Include code examples where helpful
- Follow the existing documentation structure

### Testing

- Write unit tests for new functionality
- Aim for high test coverage
- Use descriptive test names
- Test both success and error cases

## Pull Request Process

1. **Ensure all checks pass** (tests, linting, etc.)
2. **Write a clear description** of your changes
3. **Reference any related issues**
4. **Request review** from maintainers
5. **Address feedback** promptly

## Issue Reporting

When reporting issues:

1. **Check existing issues** first
2. **Use the issue template** provided
3. **Include reproduction steps**
4. **Provide system information** (OS, Python version, etc.)
5. **Include error messages** and logs

## Development Guidelines

### Adding New Features

- Discuss major features in issues first
- Keep features focused and atomic
- Consider backward compatibility
- Update tests and documentation

### Bug Fixes

- Include a test that reproduces the bug
- Fix the root cause, not just symptoms
- Update documentation if behavior changes

### Documentation

- Keep documentation up to date
- Use clear, simple language
- Include practical examples
- Test all code examples

## Release Process

Releases are handled by maintainers:

1. **Version bump** in `pyproject.toml`
2. **Update changelog**
3. **Create release tag**
4. **Build and publish** to PyPI
5. **Update documentation**

## Questions?

- **GitHub Discussions**: For general questions and discussions
- **Issues**: For bug reports and feature requests
- **Pull Requests**: For code contributions

Thank you for contributing to OParl MCP Server! 🎉
