#!/usr/bin/env python3
"""Test script to verify OParl MCP Server setup."""

import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from oparl_mcp import OParlMCPServer, OParlConfig, OParlAuthenticator
        print("✅ Core imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    try:
        from oparl_mcp.utils import format_oparl_date, build_query_params
        print("✅ Utility imports successful")
    except ImportError as e:
        print(f"❌ Utility import error: {e}")
        return False
    
    return True

def test_config():
    """Test configuration creation."""
    print("\nTesting configuration...")
    
    try:
        from oparl_mcp import OParlConfig
        
        # Test default config
        config = OParlConfig()
        assert config.base_url == "https://api.oparl.org"
        assert config.timeout == 30.0
        print("✅ Default configuration works")
        
        # Test custom config
        custom_config = OParlConfig(
            base_url="https://test.oparl.api.com",
            api_key="test-key",
            timeout=60.0
        )
        assert custom_config.base_url == "https://test.oparl.api.com"
        assert custom_config.api_key == "test-key"
        assert custom_config.timeout == 60.0
        print("✅ Custom configuration works")
        
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_openapi_spec():
    """Test OpenAPI specification loading."""
    print("\nTesting OpenAPI specification...")
    
    try:
        import json
        from pathlib import Path
        
        spec_path = Path(__file__).parent / "oparl_openapi.json"
        
        if not spec_path.exists():
            print("❌ OpenAPI specification file not found")
            return False
        
        with open(spec_path, 'r') as f:
            spec = json.load(f)
        
        assert "openapi" in spec
        assert "paths" in spec
        assert "components" in spec
        print("✅ OpenAPI specification is valid")
        
        return True
    except Exception as e:
        print(f"❌ OpenAPI specification error: {e}")
        return False

def test_server_creation():
    """Test server creation (without running)."""
    print("\nTesting server creation...")
    
    try:
        from oparl_mcp import OParlMCPServer, OParlConfig
        from unittest.mock import patch
        
        config = OParlConfig()
        
        # Mock FastMCP to avoid actual server creation
        with patch('oparl_mcp.server.FastMCP') as mock_fastmcp:
            mock_fastmcp.from_openapi.return_value = None
            
            server = OParlMCPServer(config)
            assert server.config == config
            print("✅ Server creation works")
        
        return True
    except Exception as e:
        print(f"❌ Server creation error: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 OParl MCP Server Setup Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_config,
        test_openapi_spec,
        test_server_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Setup is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
