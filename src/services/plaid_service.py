"""
Plaid API Service Integration
"""

import plaid
from plaid.api import plaid_api
from typing import Dict, Any

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id: str = client_id
        self.secret: str = secret
        self.env: str = env.lower()

        # Map environment string to Plaid host
        if self.env == 'development':
            host = "https://development.plaid.com"
        elif self.env == 'production':
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        # Initialize Plaid configuration
        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        # Initialize ApiClient and PlaidApi
        api_client = plaid.ApiClient(configuration)
        self.client: plaid_api.PlaidApi = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid service has been configured with credentials.

        Returns:
            bool: True if client_id and secret are present, False otherwise.
        """
        return bool(self.client_id and self.secret)
