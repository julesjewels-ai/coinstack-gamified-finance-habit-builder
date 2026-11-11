"""
Plaid API Service integration.
Handles connection to Plaid and related operations.
"""

import plaid
from plaid.api import plaid_api
from plaid.configuration import Configuration
from src.core.config import settings

class PlaidService:
    """Service class encapsulating Plaid API interactions."""

    def __init__(self) -> None:
        """Initializes the Plaid client based on environment configuration."""
        self.client_id = settings.PLAID_CLIENT_ID
        self.secret = settings.PLAID_SECRET
        self.env = settings.PLAID_ENV.lower()

        # Determine host based on environment string
        if self.env == "production":
            host = plaid.Environment.Production
        elif self.env == "development":
            # plaid-python deprecated the Development enum, use direct URL
            host = "https://development.plaid.com"
        else:
            host = plaid.Environment.Sandbox

        configuration = Configuration(
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
        Check if the basic credentials have been set in the environment.

        Returns:
            bool: True if CLIENT_ID and SECRET are truthy.
        """
        return bool(self.client_id and self.secret)
