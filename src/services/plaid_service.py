"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """Service for interacting with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initialize the Plaid API client.

        Args:
            client_id: Plaid client ID
            secret: Plaid secret
            env: Plaid environment string (e.g., 'sandbox', 'production')
        """
        # The 'development' env enum is deprecated, map to Sandbox
        if env.lower() == 'development':
            plaid_env = plaid.Environment.Sandbox
        elif env.lower() == 'sandbox':
            plaid_env = plaid.Environment.Sandbox
        elif env.lower() == 'production':
            plaid_env = plaid.Environment.Production
        else:
            plaid_env = plaid.Environment.Sandbox  # Default fallback

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """Returns the configured PlaidApi client."""
        return self.client
