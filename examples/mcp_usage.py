"""MCP usage example showing how to interact with OParl MCP Server."""

import asyncio
import json
from pathlib import Path
import sys

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from oparl_mcp import OParlConfig, OParlMCPServer


async def demonstrate_mcp_resources():
    """Demonstrate MCP resource access patterns."""
    print("🔍 MCP Resource Access Examples")
    print("=" * 50)
    
    # Create server configuration
    config = OParlConfig(
        base_url="https://api.oparl.org",
        server_name="OParl MCP Demo"
    )
    
    server = OParlMCPServer(config)
    
    print("📋 Available MCP Resources:")
    print("   • oparl_system - System information")
    print("   • oparl_bodies - List of parliamentary bodies")
    print("   • oparl_meetings - List of meetings")
    print("   • oparl_persons - List of people")
    print("   • oparl_papers - List of papers")
    print("   • oparl_organizations - List of organizations")
    print()
    
    print("📋 Available MCP Resource Templates:")
    print("   • oparl_meeting_{id} - Specific meeting details")
    print("   • oparl_person_{id} - Specific person profile")
    print("   • oparl_paper_{id} - Specific paper content")
    print("   • oparl_body_{id} - Specific body information")
    print()
    
    print("🔧 Available MCP Tools:")
    print("   • oparl_search - Search across OParl data")
    print("   • oparl_filter - Filter data by criteria")
    print("   • oparl_export - Export data in different formats")
    print()


async def demonstrate_oparl_objects():
    """Demonstrate OParl object types and their properties."""
    print("🏛️ OParl Object Types")
    print("=" * 50)
    
    oparl_objects = {
        "System": {
            "description": "Root system information and metadata",
            "key_properties": ["oparlVersion", "body", "created", "modified"],
            "example_id": "https://api.oparl.org/system"
        },
        "Body": {
            "description": "Parliamentary bodies (councils, committees)",
            "key_properties": ["name", "shortName", "organization", "meeting"],
            "example_id": "https://api.oparl.org/body/1"
        },
        "Organization": {
            "description": "Political parties, groups, institutions",
            "key_properties": ["name", "shortName", "body", "member"],
            "example_id": "https://api.oparl.org/organization/1"
        },
        "Person": {
            "description": "Elected officials, staff, participants",
            "key_properties": ["name", "givenName", "familyName", "body"],
            "example_id": "https://api.oparl.org/person/1"
        },
        "Meeting": {
            "description": "Parliamentary sessions and events",
            "key_properties": ["name", "start", "end", "location", "agendaItem"],
            "example_id": "https://api.oparl.org/meeting/1"
        },
        "AgendaItem": {
            "description": "Meeting agenda items and topics",
            "key_properties": ["name", "meeting", "order", "consultation"],
            "example_id": "https://api.oparl.org/agendaitem/1"
        },
        "Paper": {
            "description": "Documents, resolutions, reports",
            "key_properties": ["name", "reference", "body", "date", "file"],
            "example_id": "https://api.oparl.org/paper/1"
        },
        "Consultation": {
            "description": "Public consultations and feedback",
            "key_properties": ["name", "paper", "authoritative", "start", "end"],
            "example_id": "https://api.oparl.org/consultation/1"
        },
        "File": {
            "description": "Attachments and media files",
            "key_properties": ["name", "fileName", "mimeType", "size", "accessUrl"],
            "example_id": "https://api.oparl.org/file/1"
        },
        "Location": {
            "description": "Meeting venues and addresses",
            "key_properties": ["name", "description", "geojson", "postalCode"],
            "example_id": "https://api.oparl.org/location/1"
        }
    }
    
    for obj_type, info in oparl_objects.items():
        print(f"📄 {obj_type}")
        print(f"   Description: {info['description']}")
        print(f"   Key Properties: {', '.join(info['key_properties'])}")
        print(f"   Example ID: {info['example_id']}")
        print()


async def demonstrate_query_parameters():
    """Demonstrate common query parameters for OParl endpoints."""
    print("🔍 Query Parameters")
    print("=" * 50)
    
    query_params = {
        "limit": {
            "description": "Maximum number of results to return",
            "default": "20",
            "max": "1000",
            "example": "?limit=50"
        },
        "offset": {
            "description": "Number of results to skip (pagination)",
            "default": "0",
            "example": "?offset=20"
        },
        "search": {
            "description": "Search term for filtering results",
            "example": "?search=budget"
        },
        "start": {
            "description": "Start date for filtering (ISO 8601)",
            "example": "?start=2024-01-01T00:00:00+01:00"
        },
        "end": {
            "description": "End date for filtering (ISO 8601)",
            "example": "?end=2024-12-31T23:59:59+01:00"
        }
    }
    
    for param, info in query_params.items():
        print(f"🔧 {param}")
        print(f"   Description: {info['description']}")
        if 'default' in info:
            print(f"   Default: {info['default']}")
        if 'max' in info:
            print(f"   Maximum: {info['max']}")
        print(f"   Example: {info['example']}")
        print()


async def demonstrate_authentication():
    """Demonstrate authentication options."""
    print("🔐 Authentication Options")
    print("=" * 50)
    
    auth_methods = {
        "No Authentication": {
            "description": "Public OParl implementations",
            "example": "https://api.oparl.org",
            "config": "No API key required"
        },
        "API Key": {
            "description": "Bearer token authentication",
            "example": "Authorization: Bearer your-api-key",
            "config": "OPARL_API_KEY=your-api-key"
        },
        "Custom Headers": {
            "description": "Additional authentication headers",
            "example": "X-API-Key: your-key",
            "config": "Custom header configuration"
        }
    }
    
    for method, info in auth_methods.items():
        print(f"🔑 {method}")
        print(f"   Description: {info['description']}")
        print(f"   Example: {info['example']}")
        print(f"   Configuration: {info['config']}")
        print()


async def demonstrate_error_handling():
    """Demonstrate error handling patterns."""
    print("⚠️ Error Handling")
    print("=" * 50)
    
    error_types = {
        "404 Not Found": {
            "description": "Resource not found",
            "mcp_response": {
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Resource not found",
                    "details": "Meeting with ID 123 not found"
                }
            }
        },
        "401 Unauthorized": {
            "description": "Authentication required",
            "mcp_response": {
                "error": {
                    "code": "UNAUTHORIZED",
                    "message": "Authentication required",
                    "details": "Invalid or missing API key"
                }
            }
        },
        "500 Internal Server Error": {
            "description": "Server error",
            "mcp_response": {
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "Internal server error",
                    "details": "Unable to connect to OParl API"
                }
            }
        },
        "Rate Limit Exceeded": {
            "description": "Too many requests",
            "mcp_response": {
                "error": {
                    "code": "RATE_LIMIT_EXCEEDED",
                    "message": "Rate limit exceeded",
                    "details": "Please wait before making more requests"
                }
            }
        }
    }
    
    for error_type, info in error_types.items():
        print(f"❌ {error_type}")
        print(f"   Description: {info['description']}")
        print(f"   MCP Response:")
        print(f"   {json.dumps(info['mcp_response'], indent=6)}")
        print()


async def main():
    """Main demonstration function."""
    print("🚀 OParl MCP Server - MCP Usage Examples")
    print("=" * 60)
    print()
    
    await demonstrate_mcp_resources()
    await demonstrate_oparl_objects()
    await demonstrate_query_parameters()
    await demonstrate_authentication()
    await demonstrate_error_handling()
    
    print("✅ MCP usage examples completed!")
    print()
    print("📚 For more information, see:")
    print("   • OParl API Overview: https://dev.oparl.org/spezifikation")
    print("   • FastMCP Documentation: https://gofastmcp.com")
    print("   • Model Context Protocol: https://modelcontextprotocol.io")


if __name__ == "__main__":
    asyncio.run(main())
