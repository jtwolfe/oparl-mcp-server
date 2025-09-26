"""Main MCP server implementation for OParl API."""

import json
import logging
from pathlib import Path
from typing import Any, Optional

import httpx
from fastmcp import FastMCP
from fastmcp.server.openapi import MCPType, RouteMap

from .config import OParlConfig

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OParlMCPServer:
    """OParl MCP Server implementation."""

    def __init__(self, config: Optional[OParlConfig] = None):
        """Initialize the OParl MCP Server.

        Args:
            config: Configuration object. If None, uses default configuration.
        """
        self.config = config or OParlConfig()
        self.mcp: Optional[FastMCP] = None
        self._setup_server()

    def _setup_server(self) -> None:
        """Set up the MCP server with OpenAPI specification and route mapping."""
        try:
            # Load OpenAPI specification
            openapi_spec = self._load_openapi_spec()

            # Create HTTP client
            client = self._create_http_client()

            # Define route mappings for OParl-specific behavior
            route_maps = self._create_route_maps()

            # Create MCP server
            self.mcp = FastMCP.from_openapi(
                openapi_spec=openapi_spec,
                client=client,
                name=self.config.server_name,
                route_maps=route_maps,
                tags={"oparl", "parliamentary-data", "government"},
            )

            logger.info(
                f"OParl MCP Server '{self.config.server_name}' initialized successfully"
            )

        except Exception as e:
            logger.error(f"Failed to initialize OParl MCP Server: {e}")
            raise

    def _load_openapi_spec(self) -> Any:
        """Load the OpenAPI specification from file.

        Returns:
            OpenAPI specification as dictionary.
        """
        spec_path = Path(__file__).parent.parent.parent / "oparl_openapi.json"

        if not spec_path.exists():
            raise FileNotFoundError(f"OpenAPI specification not found at {spec_path}")

        with open(spec_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _create_http_client(self) -> httpx.AsyncClient:
        """Create HTTP client for OParl API.

        Returns:
            Configured HTTP client.
        """
        headers = {}

        # Add authentication if API key is provided
        if self.config.api_key:
            headers["Authorization"] = f"Bearer {self.config.api_key}"

        return httpx.AsyncClient(
            base_url=self.config.base_url, headers=headers, timeout=self.config.timeout
        )

    def _create_route_maps(self) -> list[RouteMap]:
        """Create route mappings for OParl API endpoints.

        Returns:
            List of route mapping configurations.
        """
        return [
            # Resource templates for parameterized GET requests (individual items)
            RouteMap(
                methods=["GET"],
                pattern=r".*\{.*\}.*",
                mcp_type=MCPType.RESOURCE_TEMPLATE,
                mcp_tags={"oparl", "data", "individual", "parameterized"},
            ),
            # Resources for simple GET requests (collections)
            RouteMap(
                methods=["GET"],
                pattern=r".*",
                mcp_type=MCPType.RESOURCE,
                mcp_tags={"oparl", "data", "collection", "read-only"},
            ),
            # Tools for write operations (if any)
            RouteMap(
                methods=["POST", "PUT", "DELETE"],
                pattern=r".*",
                mcp_type=MCPType.TOOL,
                mcp_tags={"oparl", "action", "write"},
            ),
            # Exclude admin or internal endpoints
            RouteMap(pattern=r".*/admin/.*", mcp_type=MCPType.EXCLUDE),
            RouteMap(pattern=r".*/internal/.*", mcp_type=MCPType.EXCLUDE),
        ]

    def run(self) -> None:
        """Run the MCP server."""
        if self.mcp is None:
            raise RuntimeError("MCP server not initialized")

        logger.info(f"Starting OParl MCP Server on {self.config.base_url}")
        self.mcp.run()

    def get_server_info(self) -> dict:
        """Get information about the MCP server.

        Returns:
            Server information dictionary.
        """
        return {
            "name": self.config.server_name,
            "version": self.config.server_version,
            "base_url": self.config.base_url,
            "oparl_version": "1.1",
            "features": [
                "System information access",
                "Body management",
                "Organization data",
                "Person profiles",
                "Meeting schedules",
                "Document access",
                "Agenda items",
                "Search functionality",
            ],
        }


def main() -> None:
    """Main entry point for the OParl MCP Server."""
    try:
        # Load configuration
        config = OParlConfig()

        # Create and run server
        server = OParlMCPServer(config)

        # Print server information
        info = server.get_server_info()
        print(f"🚀 {info['name']} v{info['version']}")
        print(f"📡 Base URL: {info['base_url']}")
        print(f"📋 OParl Version: {info['oparl_version']}")
        print(f"✨ Features: {', '.join(info['features'])}")
        print("-" * 50)

        # Run the server
        server.run()

    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


if __name__ == "__main__":
    main()
