"""
Service module for interacting with the Plaid API.
"""
from typing import Optional
import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    A service class for integrating with Plaid.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with configuration.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map environment string to plaid.Environment
        # Note: The 'development' environment was deprecated by Plaid.
        if self.env_name == 'production':
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

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is properly configured with credentials.

        Returns:
            bool: True if client_id and secret are truthy, False otherwise.
        """
        return bool(self.client_id) and bool(self.secret)
