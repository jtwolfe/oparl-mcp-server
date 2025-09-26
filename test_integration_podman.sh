#!/bin/bash
# Podman-specific integration test script

set -e

echo "🧪 Running Integration Tests with Podman"
echo "========================================"

# Check if podman is available
if ! command -v podman &> /dev/null; then
    echo "❌ Podman not found. Please install Podman first."
    exit 1
fi

echo "✅ Podman found: $(podman --version)"

# Test Python imports first
echo ""
echo "🐍 Testing Python imports..."
python -c "
from oparl_mcp import OParlMCPServer, OParlConfig
config = OParlConfig()
server = OParlMCPServer(config)
info = server.get_server_info()
print('✅ Python imports successful')
print(f'Server: {info[\"name\"]} v{info[\"version\"]}')
"

# Build container image
echo ""
echo "🔨 Building container image with Podman..."
podman build -f docker/Dockerfile -t oparl-mcp-server:test .

# Test container run
echo ""
echo "🚀 Testing container run with Podman..."
podman run --rm --name oparl-test oparl-mcp-server:test

echo ""
echo "🎉 All integration tests passed with Podman!"
