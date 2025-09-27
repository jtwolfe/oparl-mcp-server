"""Advanced usage example for OParl MCP Server with custom configuration."""

import asyncio
import os

# Add the src directory to the Python path
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from oparl_mcp import OParlConfig, OParlMCPServer


async def main():
    """Demonstrate advanced usage of OParl MCP Server."""
    print("🚀 OParl MCP Server - Advanced Usage Example")
    print("=" * 50)

    # Example 1: Custom configuration with environment variables
    print("1. Configuration with Environment Variables")
    print("-" * 40)

    # Set environment variables (in real usage, these would be set externally)
    os.environ["OPARL_BASE_URL"] = "https://api.oparl.org"
    os.environ["OPARL_API_KEY"] = "your-api-key-here"
    os.environ["OPARL_TIMEOUT"] = "60.0"
    os.environ["OPARL_LOG_LEVEL"] = "DEBUG"

    config = OParlConfig()
    print(f"Base URL: {config.base_url}")
    print(f"API Key: {'Set' if config.api_key else 'Not set'}")
    print(f"Timeout: {config.timeout}s")
    print(f"Log Level: {config.log_level}")
    print()

    # Example 2: Custom server configuration
    print("2. Custom Server Configuration")
    print("-" * 40)

    custom_config = OParlConfig(
        base_url="https://custom.oparl.api.com",
        api_key="custom-api-key",
        timeout=45.0,
        server_name="Custom OParl MCP Server",
        server_version="1.0.0",
        log_level="INFO",
    )

    print(f"Server Name: {custom_config.server_name}")
    print(f"Server Version: {custom_config.server_version}")
    print(f"Base URL: {custom_config.base_url}")
    print(f"API Key: {'Set' if custom_config.api_key else 'Not set'}")
    print(f"Timeout: {custom_config.timeout}s")
    print()

    # Example 3: Create server with custom configuration
    print("3. Server Creation and Information")
    print("-" * 40)

    try:
        server = OParlMCPServer(custom_config)
        info = server.get_server_info()

        print("✅ Server created successfully!")
        print(f"   Name: {info['name']}")
        print(f"   Version: {info['version']}")
        print(f"   Base URL: {info['base_url']}")
        print(f"   OParl Version: {info['oparl_version']}")
        print()

        print("Available Features:")
        for feature in info["features"]:
            print(f"   ✨ {feature}")
        print()

    except Exception as e:
        print(f"❌ Error creating server: {e}")
        print()

    # Example 4: Different OParl implementations
    print("4. Different OParl Implementations")
    print("-" * 40)

    implementations = [
        ("Generic OParl API", "https://api.oparl.org"),
        ("Munich City Council", "https://oparl.muenchen.de"),
        ("Cologne City Council", "https://oparl.koeln.de"),
        ("Hamburg Parliament", "https://oparl.hamburg.de"),
    ]

    for name, url in implementations:
        print(f"   {name}: {url}")
    print()

    print("📝 Note: Each implementation may have different:")
    print("   - Authentication requirements")
    print("   - Available data")
    print("   - API endpoints")
    print("   - Rate limits")
    print()

    print("✅ Advanced configuration examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
