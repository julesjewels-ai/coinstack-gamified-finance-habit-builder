"""
Plaid API integration service.
Handles connecting to the Plaid API and fetching data.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """Service class for interacting with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map environment string to Plaid environment URLs
        if self.env_name == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env_name == 'development':
            # Plaid SDK deprecated Development enum, explicitly set URL
            host = 'https://development.plaid.com'
        elif self.env_name == 'production':
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        # Initialize the Plaid client
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
        """Checks if the Plaid client is configured with credentials."""
        return bool(self.client_id and self.secret)
