"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class to handle interactions with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id: The Plaid Client ID.
            secret: The Plaid Secret.
            env: The Plaid environment ('sandbox' or 'production'). 'development' is treated as 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map environment string to Plaid environment
        plaid_env = plaid.Environment.Sandbox
        if self.env_name == 'production':
            plaid_env = plaid.Environment.Production

        # The Python SDK uses a Configuration object
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
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id) and bool(self.secret)
