"""
Plaid API integration service.
Handles connecting to Plaid, linking accounts, and fetching transactions.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api


class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid client ID.
            secret: The Plaid secret.
            environment: The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        # Determine the correct host environment
        if self.environment == "sandbox":
            host = plaid.Environment.Sandbox
        elif self.environment == "production":
            host = plaid.Environment.Production
        elif self.environment == "development":
            # The 'Development' enum was deprecated; use the URL directly
            host = "https://development.plaid.com"
        else:
            # Default to sandbox if unknown
            host = plaid.Environment.Sandbox

        # Configure the Plaid client
        configuration = plaid.Configuration(
            host=host,
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
            The configured Plaid API client.
        """
        return self.client
