# Server API Reference

API reference for the OParl MCP Server.

## OParlMCPServer

Main server class for the OParl MCP Server.

### Constructor

```python
OParlMCPServer(config: Optional[OParlConfig] = None)
```

**Parameters:**
- `config` (Optional[OParlConfig]): Configuration object. If None, uses default configuration.

### Methods

#### `run()`
Start the MCP server.

```python
server.run()
```

#### `get_server_info() -> dict`
Get information about the MCP server.

**Returns:**
- `dict`: Server information including name, version, base URL, and features.

**Example:**
```python
info = server.get_server_info()
print(f"Server: {info['name']}")
print(f"Version: {info['version']}")
print(f"Features: {info['features']}")
```

## OParlConfig

Configuration class for OParl MCP Server.

### Constructor

```python
OParlConfig(
    base_url: str = "https://api.oparl.org",
    api_key: Optional[str] = None,
    timeout: float = 30.0,
    server_name: str = "OParl MCP Server",
    server_version: str = "0.1.0",
    log_level: str = "INFO"
)
```

**Parameters:**
- `base_url` (str): Base URL of the OParl API
- `api_key` (Optional[str]): API key for authentication
- `timeout` (float): Request timeout in seconds
- `server_name` (str): Server name
- `server_version` (str): Server version
- `log_level` (str): Logging level

### Environment Variables

The configuration can be loaded from environment variables with the `OPARL_` prefix:

- `OPARL_BASE_URL`: Base URL of the OParl API
- `OPARL_API_KEY`: API key for authentication
- `OPARL_TIMEOUT`: Request timeout in seconds
- `OPARL_LOG_LEVEL`: Logging level
- `OPARL_SERVER_NAME`: Server name
- `OPARL_SERVER_VERSION`: Server version

## OParlAuthenticator

Authentication handler for OParl API.

### Constructor

```python
OParlAuthenticator(api_key: Optional[str] = None)
```

**Parameters:**
- `api_key` (Optional[str]): API key for authentication (optional).

### Methods

#### `get_auth_headers() -> Dict[str, str]`
Get authentication headers for API requests.

**Returns:**
- `Dict[str, str]`: Dictionary containing authentication headers.

#### `set_token(token: str) -> None`
Set authentication token.

**Parameters:**
- `token` (str): Authentication token.

#### `is_authenticated() -> bool`
Check if authenticator has valid credentials.

**Returns:**
- `bool`: True if authenticated, False otherwise.

## Utility Functions

### `format_oparl_date(date_obj: Optional[Any]) -> Optional[str]`
Format date object for OParl API.

**Parameters:**
- `date_obj` (Optional[Any]): Date object to format.

**Returns:**
- `Optional[str]`: Formatted date string or None.

### `build_query_params(**kwargs) -> Dict[str, Any]`
Build query parameters for OParl API requests.

**Parameters:**
- `**kwargs`: Query parameters including limit, offset, search, start_date, end_date.

**Returns:**
- `Dict[str, Any]`: Dictionary of query parameters.

### `validate_oparl_url(url: str, base_url: str) -> bool`
Validate if URL is a valid OParl resource URL.

**Parameters:**
- `url` (str): URL to validate.
- `base_url` (str): Base URL of the OParl API.

**Returns:**
- `bool`: True if URL is valid, False otherwise.

### `create_oparl_summary(data: Dict[str, Any]) -> str`
Create a human-readable summary of OParl data.

**Parameters:**
- `data` (Dict[str, Any]): OParl data object.

**Returns:**
- `str`: Summary string.
