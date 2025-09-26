"""Authentication handling for OParl MCP Server."""

import logging
from typing import Any, Dict, Optional

import httpx

logger = logging.getLogger(__name__)


class OParlAuthenticator:
    """Handles authentication for OParl API."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the authenticator.

        Args:
            api_key: API key for authentication (optional).
        """
        self.api_key = api_key
        self._token: Optional[str] = None

    def get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for API requests.

        Returns:
            Dictionary containing authentication headers.
        """
        headers = {}

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        elif self._token:
            headers["Authorization"] = f"Bearer {self._token}"

        return headers

    def set_token(self, token: str) -> None:
        """Set authentication token.

        Args:
            token: Authentication token.
        """
        self._token = token
        logger.info("Authentication token updated")

    def clear_token(self) -> None:
        """Clear authentication token."""
        self._token = None
        logger.info("Authentication token cleared")

    def is_authenticated(self) -> bool:
        """Check if authenticator has valid credentials.

        Returns:
            True if authenticated, False otherwise.
        """
        return bool(self.api_key or self._token)

    async def validate_credentials(self, base_url: str) -> bool:
        """Validate authentication credentials against the API.

        Args:
            base_url: Base URL of the OParl API.

        Returns:
            True if credentials are valid, False otherwise.
        """
        if not self.is_authenticated():
            return True  # No authentication required

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{base_url}/system", headers=self.get_auth_headers(), timeout=10.0
                )
                return response.status_code == 200
        except Exception as e:
            logger.error(f"Failed to validate credentials: {e}")
            return False
