"""
Plaid Service module for handling bank integration via the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from plaid.configuration import Configuration
from plaid.api_client import ApiClient

class PlaidService:
    """Service class encapsulating interaction with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid Service.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Plaid-python deprecated the Development enum, so we handle it explicitly.
        if self.env_name == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env_name == 'production':
            host = plaid.Environment.Production
        elif self.env_name == 'development':
            host = 'https://development.plaid.com'
        else:
            host = plaid.Environment.Sandbox # Default to sandbox

        self.configuration = Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        self.api_client = ApiClient(self.configuration)
        self.client = plaid_api.PlaidApi(self.api_client)
