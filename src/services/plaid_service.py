"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """Service to interact with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with API credentials and environment.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Configure host based on environment
        if self.env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env == 'production':
            host = plaid.Environment.Production
        elif self.env == 'development':
            # Plaid python deprecated the Development enum, use direct URL
            host = 'https://development.plaid.com'
        else:
            host = plaid.Environment.Sandbox # Default to sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
