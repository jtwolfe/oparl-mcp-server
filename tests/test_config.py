"""Tests for OParl configuration."""

import os
from unittest.mock import patch

import pytest

from oparl_mcp.config import OParlConfig


class TestOParlConfig:
    """Test cases for OParlConfig."""

    def test_default_config(self):
        """Test default configuration values."""
        config = OParlConfig()

        assert config.base_url == "https://api.oparl.org"
        assert config.api_key is None
        assert config.timeout == 30.0
        assert config.server_name == "OParl MCP Server"
        assert config.server_version == "0.1.0"
        assert config.log_level == "INFO"

    def test_custom_config(self):
        """Test custom configuration values."""
        config = OParlConfig(
            base_url="https://custom.oparl.api.com",
            api_key="test-key",
            timeout=60.0,
            server_name="Custom Server",
            server_version="2.0.0",
            log_level="DEBUG",
        )

        assert config.base_url == "https://custom.oparl.api.com"
        assert config.api_key == "test-key"
        assert config.timeout == 60.0
        assert config.server_name == "Custom Server"
        assert config.server_version == "2.0.0"
        assert config.log_level == "DEBUG"

    def test_env_prefix(self):
        """Test environment variable prefix."""
        with patch.dict(
            os.environ,
            {
                "OPARL_BASE_URL": "https://env.oparl.api.com",
                "OPARL_API_KEY": "env-key",
                "OPARL_TIMEOUT": "45.0",
                "OPARL_LOG_LEVEL": "WARNING",
            },
        ):
            config = OParlConfig()

            assert config.base_url == "https://env.oparl.api.com"
            assert config.api_key == "env-key"
            assert config.timeout == 45.0
            assert config.log_level == "WARNING"

    def test_env_file_loading(self):
        """Test loading configuration from .env file."""
        # This test would require creating a temporary .env file
        # For now, we'll just test that the config class is set up correctly
        config = OParlConfig()

        # Verify that the config class has the right settings
        assert hasattr(config, "Config")
        assert hasattr(config.Config, "env_prefix")
        assert hasattr(config.Config, "env_file")
        assert config.Config.env_prefix == "OPARL_"
        assert config.Config.env_file == ".env"


if __name__ == "__main__":
    pytest.main([__file__])
