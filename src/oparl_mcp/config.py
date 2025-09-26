"""Configuration management for OParl MCP Server."""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class OParlConfig(BaseSettings):
    """Configuration settings for OParl MCP Server."""
    
    # API Configuration
    base_url: str = "https://api.oparl.org"
    api_key: Optional[str] = None
    timeout: float = 30.0
    
    # MCP Configuration
    server_name: str = "OParl MCP Server"
    server_version: str = "0.1.0"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_prefix = "OPARL_"
        env_file = ".env"
