#!/usr/bin/env python3
"""Test script to verify integration test logic works locally."""

import subprocess
import sys
import os

def test_container_build():
    """Test container build process (Docker/Podman)."""
    print("🔨 Testing container build...")
    
    # Try Podman first, then Docker
    for cmd in ["podman", "docker"]:
        try:
            result = subprocess.run([
                cmd, "build", "-f", "docker/Dockerfile", 
                "-t", "oparl-mcp-server:test", "."
            ], capture_output=True, text=True, check=True)
            print(f"✅ Container build successful using {cmd}")
            return True, cmd
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    print("❌ Container build failed: Neither podman nor docker found")
    return False, None

def test_container_run(container_cmd):
    """Test container run process."""
    print("🚀 Testing container run...")
    try:
        result = subprocess.run([
            container_cmd, "run", "--rm", "--name", "oparl-test", 
            "oparl-mcp-server:test"
        ], capture_output=True, text=True, check=True)
        print("✅ Container run successful")
        print("Container output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Container run failed: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def test_python_imports():
    """Test Python imports work correctly."""
    print("🐍 Testing Python imports...")
    try:
        # Test in virtual environment
        result = subprocess.run([
            "python", "-c", 
            "from oparl_mcp import OParlMCPServer, OParlConfig; "
            "config = OParlConfig(); "
            "server = OParlMCPServer(config); "
            "info = server.get_server_info(); "
            "print('✅ Python imports successful'); "
            "print(f'Server: {info[\"name\"]} v{info[\"version\"]}')"
        ], capture_output=True, text=True, check=True)
        print("✅ Python imports successful")
        print("Python output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Python imports failed: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def main():
    """Run all integration tests."""
    print("🧪 Running Integration Tests")
    print("=" * 50)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Not running in a virtual environment")
    
    # First test Python imports
    print(f"\n📋 Running Python Imports...")
    python_success = test_python_imports()
    results = [("Python Imports", python_success)]
    
    # Then test container build and run
    print(f"\n📋 Running Container Build...")
    build_success, container_cmd = test_container_build()
    results.append(("Container Build", build_success))
    
    if build_success and container_cmd:
        print(f"\n📋 Running Container Run...")
        run_success = test_container_run(container_cmd)
        results.append(("Container Run", run_success))
    else:
        results.append(("Container Run", False))
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    all_passed = all(success for _, success in results)
    if all_passed:
        print("\n🎉 All integration tests passed!")
        return 0
    else:
        print("\n💥 Some integration tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
