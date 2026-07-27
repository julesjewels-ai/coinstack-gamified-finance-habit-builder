"""
Service module for handling Plaid API integration.
"""

from typing import Dict, Any, Optional
import plaid
from plaid.api import plaid_api
from src.core.config import Settings


class PlaidService:
    """
    A service class for integrating with the Plaid API.

    Handles initialization of the Plaid client and provides methods for interacting
    with Plaid endpoints for banking data retrieval.
    """

    def __init__(self, settings: Settings) -> None:
        """
        Initializes the PlaidService and authenticates the Plaid client.

        Args:
            settings (Settings): Application configuration containing Plaid credentials.
        """
        self.settings = settings
        self.env = settings.PLAID_ENV.lower()

        # Map environment string to plaid-python Environment class variable
        host = plaid.Environment.Sandbox
        if self.env == "production":
            host = plaid.Environment.Production
        elif self.env == "development":
            # Plaid deprecated the 'development' environment. Map to Sandbox as per memory rules.
            host = plaid.Environment.Sandbox

        # Plaid Configuration requires host and api_key dictionary
        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.settings.PLAID_CLIENT_ID,
                'secret': self.settings.PLAID_SECRET,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client instance.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client.
        """
        return self.client
