"""Basic usage example for OParl MCP Server."""

import asyncio
import json

# Add the src directory to the Python path
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from oparl_mcp import OParlConfig, OParlMCPServer


async def main():
    """Demonstrate basic usage of OParl MCP Server."""
    print("🚀 OParl MCP Server - Basic Usage Example")
    print("=" * 50)

    # Create configuration
    config = OParlConfig(
        base_url="https://api.oparl.org", server_name="OParl MCP Demo Server"
    )

    # Create server instance
    server = OParlMCPServer(config)

    # Display server information
    info = server.get_server_info()
    print(f"Server: {info['name']}")
    print(f"Version: {info['version']}")
    print(f"Base URL: {info['base_url']}")
    print(f"OParl Version: {info['oparl_version']}")
    print()

    # List available features
    print("Available Features:")
    for feature in info["features"]:
        print(f"  ✨ {feature}")
    print()

    # Note: In a real MCP client, you would use the MCP protocol
    # to interact with the server. This example shows the server setup.
    print("📝 Note: This example shows server setup.")
    print("   To interact with the server, use an MCP client that")
    print("   connects to this server via the MCP protocol.")
    print()

    print("🔧 Server Configuration:")
    print(f"   Timeout: {config.timeout}s")
    print(f"   Log Level: {config.log_level}")
    print(f"   API Key: {'Set' if config.api_key else 'Not set'}")
    print()

    print("✅ OParl MCP Server is ready to use!")


if __name__ == "__main__":
    asyncio.run(main())
