"""
Plaid API integration service.
Handles connecting to Plaid, linking accounts, and fetching data.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """Service to interact with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid Service.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox' or 'production'). 'development' maps to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret

        # Map environment string to Plaid environment.
        # Note: Plaid's development environment is deprecated.
        env_lower = env.lower()
        if env_lower == 'production':
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
        """Check if the Plaid service has been configured with credentials."""
        return bool(self.client_id and self.secret)
