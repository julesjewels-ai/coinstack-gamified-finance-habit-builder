"""
Plaid API integration service.
Handles connecting to Plaid, fetching transactions, and managing links.
"""

import plaid
from plaid.api import plaid_api
from typing import Dict, Any

class PlaidService:
    """Service to interact with the Plaid API."""

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox' or 'production').
                               'development' is deprecated and maps to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.environment_name = environment.lower()

        # Map environment string to Plaid Environment enum
        if self.environment_name == 'production':
            plaid_env = plaid.Environment.Production
        else:
            # Map 'development' or 'sandbox' to Sandbox
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

    def get_client(self) -> plaid_api.PlaidApi:
        """Returns the initialized Plaid API client."""
        return self.client
