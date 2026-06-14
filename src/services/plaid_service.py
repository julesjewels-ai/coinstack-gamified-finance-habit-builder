"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid Client ID.
            secret: The Plaid Secret.
            env: The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        plaid_env = plaid.Environment.Sandbox
        if self.env == 'production':
            plaid_env = plaid.Environment.Production
        elif self.env == 'development':
            plaid_env = plaid.Environment.Sandbox # map development to Sandbox per instructions

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def test_connection(self) -> bool:
        """
        A placeholder method to test if the client is initialized.
        Returns True if client initialization succeeded.
        """
        return self.client is not None
