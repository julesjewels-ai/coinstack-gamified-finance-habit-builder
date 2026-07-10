"""
Plaid service module.
Handles integration with the Plaid API for bank connectivity.
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
        Initializes the Plaid client using the provided settings.

        Args:
            settings: The application settings containing Plaid credentials.
        """
        self.client_id = settings.PLAID_CLIENT_ID
        self.secret = settings.PLAID_SECRET
        self.env = settings.PLAID_ENV.lower()

        if self.env == 'sandbox':
            plaid_env = plaid.Environment.Sandbox
        elif self.env == 'production':
            plaid_env = plaid.Environment.Production
        else:
            plaid_env = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client.

        Returns:
            The PlaidApi instance.
        """
        return self.client
