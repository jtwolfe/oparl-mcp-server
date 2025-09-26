# Utilities API Reference

Utility functions for OParl MCP Server.

## Date Formatting

### `format_oparl_date(date_obj: Optional[Any]) -> Optional[str]`
Format date object for OParl API.

**Parameters:**
- `date_obj` (Optional[Any]): Date object to format.

**Returns:**
- `Optional[str]`: Formatted date string or None.

**Example:**
```python
from oparl_mcp.utils import format_oparl_date
from datetime import datetime

date_str = format_oparl_date(datetime.now())
print(date_str)  # "2024-01-15T10:30:00Z"
```

## Query Parameters

### `build_query_params(**kwargs) -> Dict[str, Any]`
Build query parameters for OParl API requests.

**Parameters:**
- `**kwargs`: Query parameters including limit, offset, search, start_date, end_date.

**Returns:**
- `Dict[str, Any]`: Dictionary of query parameters.

**Example:**
```python
from oparl_mcp.utils import build_query_params

params = build_query_params(
    limit=10,
    offset=0,
    search="budget",
    start_date="2024-01-01",
    end_date="2024-12-31"
)
print(params)  # {"limit": 10, "offset": 0, "search": "budget", ...}
```

## URL Validation

### `validate_oparl_url(url: str, base_url: str) -> bool`
Validate if URL is a valid OParl resource URL.

**Parameters:**
- `url` (str): URL to validate.
- `base_url` (str): Base URL of the OParl API.

**Returns:**
- `bool`: True if URL is valid, False otherwise.

**Example:**
```python
from oparl_mcp.utils import validate_oparl_url

is_valid = validate_oparl_url(
    "https://api.oparl.org/body/1",
    "https://api.oparl.org"
)
print(is_valid)  # True
```

## Data Summarization

### `create_oparl_summary(data: Dict[str, Any]) -> str`
Create a human-readable summary of OParl data.

**Parameters:**
- `data` (Dict[str, Any]): OParl data object.

**Returns:**
- `str`: Summary string.

**Example:**
```python
from oparl_mcp.utils import create_oparl_summary

meeting_data = {
    "name": "City Council Meeting",
    "start": "2024-01-15T18:00:00Z",
    "location": {"name": "City Hall"}
}

summary = create_oparl_summary(meeting_data)
print(summary)  # "City Council Meeting on 2024-01-15 at City Hall"
```
