# MCP Components

Understanding the Model Context Protocol components provided by OParl MCP Server.

## Resources

Resources provide read-only access to data collections.

### System Information
- **Endpoint**: `/system`
- **Description**: Root system information and metadata
- **Type**: Resource

### Body Collections
- **Endpoint**: `/body`
- **Description**: Lists of parliamentary bodies
- **Type**: Resource
- **Parameters**: `limit`, `offset`

### Organization Data
- **Endpoint**: `/body/{bodyId}/organization`
- **Description**: Political parties and groups
- **Type**: Resource
- **Parameters**: `limit`, `offset`

### Person Profiles
- **Endpoint**: `/body/{bodyId}/person`
- **Description**: Elected officials and staff
- **Type**: Resource
- **Parameters**: `limit`, `offset`

### Meeting Schedules
- **Endpoint**: `/body/{bodyId}/meeting`
- **Description**: Upcoming and past meetings
- **Type**: Resource
- **Parameters**: `limit`, `offset`, `start`, `end`

### Document Collections
- **Endpoint**: `/body/{bodyId}/paper`
- **Description**: Papers and reports
- **Type**: Resource
- **Parameters**: `limit`, `offset`, `search`

## Resource Templates

Resource templates provide parameterized access to individual items.

### Individual Items
- **Meeting Details**: `/meeting/{meetingId}`
- **Person Profile**: `/person/{personId}`
- **Organization Details**: `/organization/{organizationId}`
- **Document Access**: `/paper/{paperId}`

## Tools

Tools provide functionality for actions and operations.

### Search Operations
- Find specific data across the system
- Filter by various criteria
- Advanced query capabilities

### Data Operations
- Export data in different formats
- Validate data integrity
- Transform data structures

## Usage Examples

### Accessing a Resource
```python
# Get system information
system_info = await client.get_resource("system")

# Get list of bodies
bodies = await client.get_resource("body", {"limit": 10})
```

### Using Resource Templates
```python
# Get specific meeting
meeting = await client.get_resource_template("meeting", {"meetingId": "123"})

# Get specific person
person = await client.get_resource_template("person", {"personId": "456"})
```

### Using Tools
```python
# Search for documents
results = await client.call_tool("search_papers", {"query": "budget"})

# Export data
export = await client.call_tool("export_meetings", {"format": "json"})
```
