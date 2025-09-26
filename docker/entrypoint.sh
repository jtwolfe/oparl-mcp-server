#!/bin/bash
set -e

echo "🚀 Starting OParl MCP Server Container..."

# Test the server initialization
echo "Testing server initialization..."
python -c "
from oparl_mcp import OParlMCPServer, OParlConfig
config = OParlConfig()
server = OParlMCPServer(config)
info = server.get_server_info()
print('✅ OParl MCP Server initialized successfully')
print(f'Server: {info[\"name\"]} v{info[\"version\"]}')
print(f'Base URL: {info[\"base_url\"]}')
print(f'Features: {len(info[\"features\"])} available')
"

echo "✅ Container test completed successfully"

# If we reach here, the server can be initialized
# For a real deployment, you would start the server here
# For testing, we just verify it can be initialized
