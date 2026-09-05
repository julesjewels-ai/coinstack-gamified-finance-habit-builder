"""
Service class for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Encapsulates interactions with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment (sandbox or production). 'development' is mapped to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map development to sandbox as the 'development' enum is deprecated
        if self.env_name == 'development':
            self.env_name = 'sandbox'

        # Set the plaid environment host
        if self.env_name == 'production':
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        # Initialize the Plaid API client configuration
        self.configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        self.api_client = plaid.ApiClient(self.configuration)
        self.client = plaid_api.PlaidApi(self.api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is properly configured with credentials.

        Returns:
            bool: True if properly configured, False otherwise.
        """
        return bool(self.client_id and self.secret)
