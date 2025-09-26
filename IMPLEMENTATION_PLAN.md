# OParl MCP Server Implementation Plan

## Project Overview

This project aims to create a Model Context Protocol (MCP) server for the OParl API using FastMCP. OParl is a standardized interface for parliamentary information systems that provides structured access to parliamentary data such as meetings, documents, organizations, and more.

## Research Findings

### OParl API Analysis
- **Specification**: OParl 1.1 is a standardized web service interface for parliamentary information systems
- **Base URL**: Various implementations exist (e.g., `https://api.oparl.org`, city-specific implementations)
- **Data Types**: System, Body, Organization, Person, Meeting, AgendaItem, Paper, Consultation, File, Location
- **Authentication**: Most implementations are public, but some may require API keys
- **OpenAPI Spec**: No official OpenAPI specification exists - needs to be created

### FastMCP Capabilities
- **OpenAPI Integration**: Can generate MCP servers from OpenAPI specifications
- **Route Mapping**: Customizable mapping of API endpoints to MCP components (Tools, Resources, ResourceTemplates)
- **Authentication**: Supports various auth methods (Bearer tokens, API keys)
- **Deployment**: Supports local, cloud, and containerized deployments

## Technical Implementation Plan

### Phase 1: Environment Setup and Dependencies

1. **Python Environment**
   - Python 3.8+ required
   - Virtual environment setup
   - Dependency management with requirements.txt

2. **Core Dependencies**
   ```bash
   pip install fastmcp httpx pydantic
   ```

3. **Development Dependencies**
   ```bash
   pip install pytest black isort mypy
   ```

### Phase 2: OpenAPI Specification Creation

Since OParl doesn't provide an official OpenAPI specification, we need to create one based on the OParl 1.1 specification:

1. **Research OParl Endpoints**
   - Analyze existing OParl implementations
   - Document common endpoint patterns
   - Identify data models and relationships

2. **Create OpenAPI Specification**
   - Generate `oparl-openapi.json` based on OParl 1.1 spec
   - Include all standard OParl object types
   - Define proper request/response schemas
   - Add authentication schemes if needed

3. **Validate Specification**
   - Test with OpenAPI validators
   - Ensure compatibility with FastMCP

### Phase 3: MCP Server Implementation

1. **Basic Server Setup**
   ```python
   from fastmcp import FastMCP
   import httpx
   
   # Load OpenAPI spec
   with open('oparl-openapi.json') as f:
       openapi_spec = json.load(f)
   
   # Create HTTP client
   client = httpx.AsyncClient(base_url="https://api.oparl.org")
   
   # Create MCP server
   mcp = FastMCP.from_openapi(
       openapi_spec=openapi_spec,
       client=client,
       name="OParl MCP Server"
   )
   ```

2. **Route Mapping Strategy**
   - **GET endpoints** → MCP Resources (for data retrieval)
   - **GET with parameters** → MCP ResourceTemplates (for parameterized queries)
   - **POST/PUT/DELETE** → MCP Tools (for actions)
   - **Admin endpoints** → Excluded

3. **Custom Route Maps**
   ```python
   from fastmcp.server.openapi import RouteMap, MCPType
   
   route_maps = [
       # Resource templates for parameterized GET requests
       RouteMap(
           methods=["GET"], 
           pattern=r".*\{.*\}.*", 
           mcp_type=MCPType.RESOURCE_TEMPLATE,
           mcp_tags={"oparl", "data", "parameterized"}
       ),
       # Resources for simple GET requests
       RouteMap(
           methods=["GET"], 
           pattern=r".*", 
           mcp_type=MCPType.RESOURCE,
           mcp_tags={"oparl", "data", "read-only"}
       ),
       # Tools for write operations
       RouteMap(
           methods=["POST", "PUT", "DELETE"], 
           pattern=r".*", 
           mcp_type=MCPType.TOOL,
           mcp_tags={"oparl", "action", "write"}
       ),
       # Exclude admin endpoints
       RouteMap(
           pattern=r".*/admin/.*", 
           mcp_type=MCPType.EXCLUDE
       ),
   ]
   ```

### Phase 4: Authentication and Configuration

1. **Authentication Support**
   - Bearer token authentication
   - API key support
   - Configurable base URLs for different OParl implementations

2. **Configuration Management**
   - Environment variables for API keys
   - Configurable base URLs
   - Timeout settings

3. **Error Handling**
   - Proper HTTP error handling
   - MCP-compliant error responses
   - Logging and monitoring

### Phase 5: Testing and Validation

1. **Unit Tests**
   - Test individual MCP components
   - Mock API responses
   - Test error handling

2. **Integration Tests**
   - Test with real OParl implementations
   - Validate data transformation
   - Test authentication flows

3. **MCP Client Testing**
   - Test with various MCP clients
   - Validate tool and resource functionality
   - Performance testing

### Phase 6: Documentation and Deployment

1. **Documentation**
   - API documentation
   - Setup and installation guide
   - Usage examples
   - Troubleshooting guide

2. **Deployment Options**
   - Local development server
   - Docker containerization
   - Cloud deployment (FastMCP Cloud)
   - Self-hosted deployment

## Project Structure

```
oparl-mcp-server/
├── README.md
├── IMPLEMENTATION_PLAN.md
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── oparl_openapi.json          # Generated OpenAPI specification
├── src/
│   └── oparl_mcp/
│       ├── __init__.py
│       ├── server.py           # Main MCP server implementation
│       ├── config.py           # Configuration management
│       ├── auth.py             # Authentication handling
│       └── utils.py            # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_server.py
│   ├── test_auth.py
│   └── test_utils.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── docs/
    ├── api.md
    ├── setup.md
    └── deployment.md
```

## Key Features

### MCP Components

1. **Resources**
   - System information
   - Body listings
   - Organization data
   - Person information
   - Meeting schedules
   - Document collections

2. **Resource Templates**
   - Specific meeting details
   - Individual document access
   - Person profiles
   - Organization details

3. **Tools**
   - Search functionality
   - Data filtering
   - Export operations
   - Data validation

### OParl Object Support

- **System**: Root system information
- **Body**: Parliamentary bodies (councils, committees)
- **Organization**: Political parties, groups
- **Person**: Elected officials, staff
- **Meeting**: Scheduled meetings and sessions
- **AgendaItem**: Meeting agenda items
- **Paper**: Documents, resolutions, reports
- **Consultation**: Public consultations
- **File**: Attachments and media
- **Location**: Meeting venues and addresses

## Implementation Timeline

1. **Week 1**: Environment setup, OpenAPI spec creation
2. **Week 2**: Basic MCP server implementation
3. **Week 3**: Route mapping and customization
4. **Week 4**: Authentication and configuration
5. **Week 5**: Testing and validation
6. **Week 6**: Documentation and deployment

## Success Criteria

- [ ] MCP server successfully connects to OParl APIs
- [ ] All major OParl object types accessible via MCP
- [ ] Proper error handling and logging
- [ ] Comprehensive test coverage
- [ ] Complete documentation
- [ ] Docker deployment ready
- [ ] Performance benchmarks met

## Risk Mitigation

1. **No Official OpenAPI Spec**: Create our own based on OParl 1.1 specification
2. **API Variations**: Support multiple OParl implementations with configurable base URLs
3. **Authentication Complexity**: Implement flexible auth system
4. **Performance Issues**: Implement caching and rate limiting
5. **Data Consistency**: Validate data against OParl schemas

## Next Steps

1. Create the OpenAPI specification for OParl
2. Set up the development environment
3. Implement the basic MCP server
4. Add comprehensive testing
5. Create deployment documentation
