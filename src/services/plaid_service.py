"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api
from src.core.config import Settings


class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, settings: Settings) -> None:
        """
        Initializes the Plaid client.

        Args:
            settings: The application settings object containing Plaid configuration.
        """
        self.client_id = settings.PLAID_CLIENT_ID
        self.secret = settings.PLAID_SECRET

        # Note: Plaid environments map to specific URLs.
        # The Environment class contains Sandbox and Production.
        # "development" is deprecated and maps to Sandbox if provided.
        env_str = settings.PLAID_ENV.lower()
        if env_str == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is configured with credentials.

        Returns:
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id and self.secret)
