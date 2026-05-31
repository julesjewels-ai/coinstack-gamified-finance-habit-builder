"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Encapsulates interaction with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid client ID.
            secret: The Plaid secret.
            env: The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        if self.env_name == 'production':
            self.plaid_env = plaid.Environment.Production
        else:
            # Fallback to Sandbox for anything else (including 'development', which is deprecated)
            self.plaid_env = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=self.plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the configured Plaid API client.

        Returns:
            The PlaidApi instance.
        """
        return self.client
