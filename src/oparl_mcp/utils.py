"""Utility functions for OParl MCP Server."""

import logging
from datetime import date, datetime
from typing import Any, Dict, Optional
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


def format_oparl_date(date_obj: Optional[Any]) -> Optional[str]:
    """Format date object for OParl API.

    Args:
        date_obj: Date object to format.

    Returns:
        Formatted date string or None.
    """
    if date_obj is None:
        return None

    if isinstance(date_obj, str):
        return date_obj

    if isinstance(date_obj, (datetime, date)):
        return date_obj.isoformat()

    return str(date_obj)


def build_query_params(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    search: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Build query parameters for OParl API requests.

    Args:
        limit: Maximum number of results to return.
        offset: Number of results to skip.
        search: Search term for filtering.
        start_date: Start date for filtering.
        end_date: End date for filtering.
        **kwargs: Additional query parameters.

    Returns:
        Dictionary of query parameters.
    """
    params: Dict[str, Any] = {}

    if limit is not None:
        params["limit"] = min(max(limit, 1), 1000)  # Clamp between 1 and 1000

    if offset is not None:
        params["offset"] = max(offset, 0)  # Ensure non-negative

    if search:
        params["search"] = search.strip()

    if start_date:
        params["start"] = format_oparl_date(start_date)

    if end_date:
        params["end"] = format_oparl_date(end_date)

    # Add any additional parameters
    for key, value in kwargs.items():
        if value is not None:
            params[key] = value

    return params


def validate_oparl_url(url: str, base_url: str) -> bool:
    """Validate if URL is a valid OParl resource URL.

    Args:
        url: URL to validate.
        base_url: Base URL of the OParl API.

    Returns:
        True if URL is valid, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        parsed_base = urlparse(base_url)

        # Check if URL starts with base URL
        return parsed_url.netloc == parsed_base.netloc and url.startswith(base_url)
    except Exception:
        return False


def extract_resource_id(url: str) -> Optional[str]:
    """Extract resource ID from OParl URL.

    Args:
        url: OParl resource URL.

    Returns:
        Resource ID or None if not found.
    """
    try:
        # OParl URLs typically end with the resource ID
        return url.rstrip("/").split("/")[-1]
    except Exception:
        return None


def format_oparl_response(data: Any) -> Any:
    """Format OParl API response for better readability.

    Args:
        data: Raw response data from OParl API.

    Returns:
        Formatted response data.
    """
    if isinstance(data, dict):
        # Add metadata if not present
        if "_meta" not in data:
            data["_meta"] = {
                "oparl_version": "1.1",
                "formatted_at": datetime.now().isoformat(),
                "source": "oparl-mcp-server",
            }

        # Format dates in the response
        for key, value in data.items():
            if isinstance(value, str) and key.endswith(
                ("Date", "Time", "created", "modified")
            ):
                try:
                    # Try to parse and reformat the date
                    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
                    data[key] = parsed.isoformat()
                except (ValueError, AttributeError):
                    pass  # Keep original value if parsing fails

    return data


def get_oparl_object_type(url: str) -> Optional[str]:
    """Determine OParl object type from URL.

    Args:
        url: OParl resource URL.

    Returns:
        OParl object type or None if not recognized.
    """
    url_lower = url.lower()

    if "/system" in url_lower:
        return "System"
    elif "/body" in url_lower:
        return "Body"
    elif "/organization" in url_lower:
        return "Organization"
    elif "/person" in url_lower:
        return "Person"
    elif "/meeting" in url_lower:
        return "Meeting"
    elif "/agendaitem" in url_lower:
        return "AgendaItem"
    elif "/paper" in url_lower:
        return "Paper"
    elif "/consultation" in url_lower:
        return "Consultation"
    elif "/file" in url_lower:
        return "File"
    elif "/location" in url_lower:
        return "Location"

    return None


def create_oparl_summary(data: Dict[str, Any]) -> str:
    """Create a human-readable summary of OParl data.

    Args:
        data: OParl data object.

    Returns:
        Summary string.
    """
    if not isinstance(data, dict):
        return str(data)

    obj_type = data.get("type", "Unknown")
    name = data.get("name", data.get("id", "Unknown"))

    # Extract type from URL if it's a full type URL
    if obj_type.startswith("https://schema.oparl.org/1.1/"):
        obj_type = obj_type.split("/")[-1]

    summary = f"{obj_type}: {name}"

    # Add additional context based on object type
    if obj_type == "Meeting" and "start" in data:
        summary += f" (scheduled: {data['start']})"
    elif obj_type == "Person" and "familyName" in data:
        summary += f" ({data.get('givenName', '')} {data['familyName']})"
    elif obj_type == "Paper" and "reference" in data:
        summary += f" (ref: {data['reference']})"

    return summary
