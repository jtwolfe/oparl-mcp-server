---
layout: page
title: "OParl API Overview"
description: "Comprehensive guide to the OParl API and its data structures"
permalink: /user-guide/oparl-api/
---

<div align="center">

# OParl API Overview

<img src="../../assets/images/oparl-logo.png" alt="OParl Logo" width="80" height="80">

**The OParl (Open Parliament) API is a standardized interface for accessing parliamentary information systems**

This guide provides a comprehensive overview of the OParl API, its data structures, and how it integrates with the MCP server.

</div>

## What is OParl?

OParl is a standardized web service interface that enables access to parliamentary data in a consistent format across different implementations. It provides structured access to:

- **Parliamentary bodies** (councils, committees, working groups)
- **Organizations** (political parties, groups, institutions)
- **People** (elected officials, staff, participants)
- **Meetings** (sessions, hearings, consultations)
- **Documents** (papers, resolutions, reports)
- **Agenda items** (topics, discussions, decisions)

## OParl 1.1 Specification

The current version is OParl 1.1, which defines:

- **Standardized data models** for parliamentary information
- **RESTful API endpoints** for data access
- **JSON-LD format** for data exchange
- **Consistent URL patterns** across implementations
- **Metadata standards** for data provenance

## Core OParl Objects

### 1. System
The root object that provides system-wide information and metadata.

**Key Properties:**
- `oparlVersion`: Version of the OParl specification
- `body`: List of available parliamentary bodies
- `created`: System creation timestamp
- `modified`: Last modification timestamp

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/System",
  "oparlVersion": "https://schema.oparl.org/1.1/",
  "body": ["https://oparl.example.org/body/1"],
  "created": "2024-01-01T00:00:00+01:00",
  "modified": "2024-01-15T10:30:00+01:00"
}
```

### 2. Body
Represents a parliamentary body such as a city council, committee, or working group.

**Key Properties:**
- `name`: Official name of the body
- `shortName`: Abbreviated name
- `organization`: Associated organizations
- `meeting`: List of meetings
- `legislativeTerm`: Current legislative period

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Body",
  "id": "https://oparl.example.org/body/1",
  "name": "Munich City Council",
  "shortName": "MCC",
  "organization": ["https://oparl.example.org/organization/1"],
  "meeting": ["https://oparl.example.org/meeting/1"]
}
```

### 3. Organization
Represents political parties, groups, or institutional organizations.

**Key Properties:**
- `name`: Organization name
- `shortName`: Abbreviated name
- `body`: Associated parliamentary body
- `member`: List of members
- `classification`: Type of organization

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Organization",
  "id": "https://oparl.example.org/organization/1",
  "name": "Social Democratic Party",
  "shortName": "SPD",
  "body": "https://oparl.example.org/body/1",
  "member": ["https://oparl.example.org/person/1"]
}
```

### 4. Person
Represents elected officials, staff, or other participants.

**Key Properties:**
- `name`: Full name
- `givenName`: First name
- `familyName`: Last name
- `body`: Associated parliamentary body
- `organization`: Political party or group
- `email`: Contact email

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Person",
  "id": "https://oparl.example.org/person/1",
  "name": "Dr. Maria Schmidt",
  "givenName": "Maria",
  "familyName": "Schmidt",
  "body": "https://oparl.example.org/body/1",
  "organization": "https://oparl.example.org/organization/1"
}
```

### 5. Meeting
Represents a parliamentary session, hearing, or consultation.

**Key Properties:**
- `name`: Meeting title
- `start`: Start date and time
- `end`: End date and time
- `location`: Meeting venue
- `agendaItem`: List of agenda items
- `participant`: List of participants

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Meeting",
  "id": "https://oparl.example.org/meeting/1",
  "name": "City Council Session",
  "start": "2024-01-15T14:00:00+01:00",
  "end": "2024-01-15T18:00:00+01:00",
  "location": "https://oparl.example.org/location/1",
  "agendaItem": ["https://oparl.example.org/agendaitem/1"]
}
```

### 6. AgendaItem
Represents a topic or item on a meeting agenda.

**Key Properties:**
- `name`: Item title
- `meeting`: Associated meeting
- `order`: Position in agenda
- `consultation`: Related consultations
- `resolution`: Decision or resolution

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/AgendaItem",
  "id": "https://oparl.example.org/agendaitem/1",
  "name": "Budget Discussion 2024",
  "meeting": "https://oparl.example.org/meeting/1",
  "order": 1,
  "consultation": ["https://oparl.example.org/consultation/1"]
}
```

### 7. Paper
Represents documents, resolutions, or reports.

**Key Properties:**
- `name`: Document title
- `reference`: Official reference number
- `body`: Associated parliamentary body
- `date`: Publication date
- `file`: Associated files

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Paper",
  "id": "https://oparl.example.org/paper/1",
  "name": "Budget Resolution 2024",
  "reference": "2024/001",
  "body": "https://oparl.example.org/body/1",
  "date": "2024-01-15T00:00:00+01:00"
}
```

### 8. Consultation
Represents public consultations or feedback processes.

**Key Properties:**
- `name`: Consultation title
- `paper`: Related document
- `authoritative`: Whether consultation is binding
- `start`: Start date
- `end`: End date

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Consultation",
  "id": "https://oparl.example.org/consultation/1",
  "name": "Public Budget Consultation",
  "paper": "https://oparl.example.org/paper/1",
  "authoritative": true,
  "start": "2024-01-01T00:00:00+01:00",
  "end": "2024-01-31T23:59:59+01:00"
}
```

### 9. File
Represents attachments, media files, or documents.

**Key Properties:**
- `name`: File name
- `fileName`: Original file name
- `mimeType`: File type
- `size`: File size in bytes
- `accessUrl`: Download URL

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/File",
  "id": "https://oparl.example.org/file/1",
  "name": "budget_2024.pdf",
  "fileName": "budget_2024.pdf",
  "mimeType": "application/pdf",
  "size": 1024000,
  "accessUrl": "https://oparl.example.org/file/1/download"
}
```

### 10. Location
Represents meeting venues, addresses, or geographical locations.

**Key Properties:**
- `name`: Location name
- `description`: Additional details
- `geojson`: Geographical coordinates
- `subLocality`: District or area
- `postalCode`: Postal code

**Example:**
```json
{
  "type": "https://schema.oparl.org/1.1/Location",
  "id": "https://oparl.example.org/location/1",
  "name": "City Hall",
  "description": "Main council chamber",
  "geojson": {
    "type": "Point",
    "coordinates": [11.5761, 48.1374]
  },
  "postalCode": "80331"
}
```

## API Endpoints

### System Endpoints
- `GET /system` - Get system information
- `GET /system/body` - List all bodies

### Body Endpoints
- `GET /body` - List all bodies
- `GET /body/{id}` - Get specific body
- `GET /body/{id}/organization` - List body organizations
- `GET /body/{id}/meeting` - List body meetings
- `GET /body/{id}/person` - List body members

### Organization Endpoints
- `GET /organization` - List all organizations
- `GET /organization/{id}` - Get specific organization
- `GET /organization/{id}/member` - List organization members

### Person Endpoints
- `GET /person` - List all people
- `GET /person/{id}` - Get specific person
- `GET /person/{id}/membership` - List person memberships

### Meeting Endpoints
- `GET /meeting` - List all meetings
- `GET /meeting/{id}` - Get specific meeting
- `GET /meeting/{id}/agendaitem` - List meeting agenda items
- `GET /meeting/{id}/participant` - List meeting participants

### Paper Endpoints
- `GET /paper` - List all papers
- `GET /paper/{id}` - Get specific paper
- `GET /paper/{id}/file` - List paper files

### Consultation Endpoints
- `GET /consultation` - List all consultations
- `GET /consultation/{id}` - Get specific consultation

### File Endpoints
- `GET /file` - List all files
- `GET /file/{id}` - Get specific file
- `GET /file/{id}/download` - Download file content

### Location Endpoints
- `GET /location` - List all locations
- `GET /location/{id}` - Get specific location

## Query Parameters

Most list endpoints support common query parameters:

- `limit` - Maximum number of results (default: 20, max: 1000)
- `offset` - Number of results to skip (default: 0)
- `search` - Search term for filtering
- `start` - Start date for filtering
- `end` - End date for filtering

## Data Relationships

OParl objects are interconnected through references:

- **System** → **Body** (one-to-many)
- **Body** → **Organization** (one-to-many)
- **Body** → **Person** (one-to-many)
- **Body** → **Meeting** (one-to-many)
- **Meeting** → **AgendaItem** (one-to-many)
- **Meeting** → **Person** (many-to-many, via participants)
- **Paper** → **File** (one-to-many)
- **AgendaItem** → **Consultation** (one-to-many)

## OParl Implementations

Various cities and institutions have implemented OParl:

- **Generic API**: `https://api.oparl.org`
- **Munich**: `https://oparl.muenchen.de`
- **Cologne**: `https://oparl.koeln.de`
- **Hamburg**: `https://oparl.hamburg.de`
- **Berlin**: `https://oparl.berlin.de`

Each implementation may have:
- Different data availability
- Varying authentication requirements
- Custom extensions
- Different rate limits

## Next Steps

- [FastMCP Integration]({{ '/user-guide/fastmcp-integration' | relative_url }}) - How FastMCP connects to OParl
- [MCP Components]({{ '/user-guide/mcp-components' | relative_url }}) - Understanding MCP resources and tools
- [Examples]({{ '/user-guide/examples' | relative_url }}) - Practical usage examples
