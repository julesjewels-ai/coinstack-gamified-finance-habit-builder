"""
Service for integrating with the Plaid API.
Handles client initialization and provides methods to communicate with Plaid.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class to encapsulate Plaid API interactions.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid SDK client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret key.
            env (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map environment string to Plaid SDK Environment
        if self.env_name in ('development', 'sandbox'):
            plaid_env = plaid.Environment.Sandbox
        elif self.env_name == 'production':
            plaid_env = plaid.Environment.Production
        else:
            # Default to Sandbox for safety if unrecognized
            plaid_env = plaid.Environment.Sandbox

        # Initialize the Plaid Configuration
        self.configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        # Initialize the API Client and Plaid API
        self.api_client = plaid.ApiClient(self.configuration)
        self.client = plaid_api.PlaidApi(self.api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client has been configured with credentials.

        Returns:
            bool: True if client_id and secret are present, False otherwise.
        """
        return bool(self.client_id and self.secret)
