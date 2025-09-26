"""Tests for OParl MCP Server."""

# Add the src directory to the Python path
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from oparl_mcp.config import OParlConfig
from oparl_mcp.server import OParlMCPServer


class TestOParlMCPServer:
    """Test cases for OParlMCPServer."""

    def test_server_initialization(self):
        """Test server initialization with default config."""
        config = OParlConfig()

        with patch("oparl_mcp.server.FastMCP") as mock_fastmcp:
            mock_fastmcp.from_openapi.return_value = Mock()

            server = OParlMCPServer(config)

            assert server.config == config
            assert server.mcp is not None
            mock_fastmcp.from_openapi.assert_called_once()

    def test_server_initialization_with_custom_config(self):
        """Test server initialization with custom config."""
        config = OParlConfig(
            base_url="https://custom.oparl.api.com", api_key="test-key", timeout=60.0
        )

        with patch("oparl_mcp.server.FastMCP") as mock_fastmcp:
            mock_fastmcp.from_openapi.return_value = Mock()

            server = OParlMCPServer(config)

            assert server.config.base_url == "https://custom.oparl.api.com"
            assert server.config.api_key == "test-key"
            assert server.config.timeout == 60.0

    def test_get_server_info(self):
        """Test getting server information."""
        config = OParlConfig(
            server_name="Test Server",
            server_version="1.0.0",
            base_url="https://test.oparl.api.com",
        )

        with patch("oparl_mcp.server.FastMCP") as mock_fastmcp:
            mock_fastmcp.from_openapi.return_value = Mock()

            server = OParlMCPServer(config)
            info = server.get_server_info()

            assert info["name"] == "Test Server"
            assert info["version"] == "1.0.0"
            assert info["base_url"] == "https://test.oparl.api.com"
            assert info["oparl_version"] == "1.1"
            assert "features" in info
            assert isinstance(info["features"], list)

    def test_load_openapi_spec_file_not_found(self):
        """Test handling when OpenAPI spec file is not found."""
        config = OParlConfig()

        with patch("oparl_mcp.server.Path.exists", return_value=False):
            with pytest.raises(FileNotFoundError):
                OParlMCPServer(config)

    def test_create_route_maps(self):
        """Test route map creation."""
        config = OParlConfig()

        with patch("oparl_mcp.server.FastMCP") as mock_fastmcp:
            mock_fastmcp.from_openapi.return_value = Mock()

            server = OParlMCPServer(config)
            route_maps = server._create_route_maps()

            assert len(route_maps) >= 4  # Should have at least 4 route maps
            assert all(hasattr(route_map, "mcp_type") for route_map in route_maps)

    def test_run_without_initialization(self):
        """Test running server without proper initialization."""
        config = OParlConfig()
        server = OParlMCPServer.__new__(OParlMCPServer)
        server.mcp = None

        with pytest.raises(RuntimeError, match="MCP server not initialized"):
            server.run()


if __name__ == "__main__":
    pytest.main([__file__])
