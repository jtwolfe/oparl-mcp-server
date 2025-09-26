# OParl Objects

Understanding the OParl object types supported by the MCP server.

## Supported Object Types

| Object Type | Description | MCP Type |
|-------------|-------------|----------|
| System | Root system information | Resource |
| Body | Parliamentary bodies | Resource/ResourceTemplate |
| Organization | Political parties, groups | Resource/ResourceTemplate |
| Person | Elected officials, staff | Resource/ResourceTemplate |
| Meeting | Scheduled meetings | Resource/ResourceTemplate |
| AgendaItem | Meeting agenda items | Resource/ResourceTemplate |
| Paper | Documents, resolutions | Resource/ResourceTemplate |
| Consultation | Public consultations | Resource/ResourceTemplate |
| File | Attachments and media | Resource/ResourceTemplate |
| Location | Meeting venues | Resource/ResourceTemplate |

## Object Properties

### System
- `id`: Unique identifier
- `type`: Object type identifier
- `oparlVersion`: OParl version used
- `body`: URL to bodies list
- `name`: System name
- `website`: System website
- `contactEmail`: Contact email
- `created`: Creation timestamp
- `modified`: Last modification timestamp

### Body
- `id`: Unique identifier
- `type`: Object type identifier
- `system`: URL to system
- `name`: Body name
- `shortName`: Short name or abbreviation
- `website`: Body website
- `email`: Contact email
- `organization`: URL to organizations list
- `person`: URL to persons list
- `meeting`: URL to meetings list
- `paper`: URL to papers list

### Person
- `id`: Unique identifier
- `type`: Object type identifier
- `body`: URL to body
- `name`: Full name
- `familyName`: Family name
- `givenName`: Given name
- `title`: Academic or professional titles
- `affiliation`: URLs to organizations
- `email`: Email address
- `phone`: Phone number
- `status`: Person status

### Meeting
- `id`: Unique identifier
- `type`: Object type identifier
- `body`: URL to body
- `name`: Meeting name
- `meetingState`: State (scheduled, cancelled, took place)
- `start`: Start time
- `end`: End time
- `location`: URL to location
- `organization`: URLs to organizations
- `participant`: URLs to participants
- `agendaItem`: URL to agenda items list

## Data Relationships

```
System
├── Body (multiple)
│   ├── Organization (multiple)
│   ├── Person (multiple)
│   ├── Meeting (multiple)
│   │   └── AgendaItem (multiple)
│   └── Paper (multiple)
│       └── File (multiple)
└── Location (multiple)
```

## Access Patterns

### Hierarchical Access
1. Start with system information
2. Get list of bodies
3. Access specific body details
4. Navigate to related objects

### Direct Access
- Use resource templates for direct object access
- Provide object ID for immediate access
- Useful for known object references

### Search and Filter
- Use tools for complex queries
- Filter by date ranges, keywords, types
- Combine multiple criteria for precise results
