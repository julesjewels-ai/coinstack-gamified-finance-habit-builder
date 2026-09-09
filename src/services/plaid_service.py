"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class to handle Plaid API initialization and interactions.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the Plaid Service.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment_name = environment.lower()

        # Map environment string to Plaid host URL
        if self.environment_name == 'production':
            host = plaid.Environment.Production
        elif self.environment_name == 'development':
            host = "https://development.plaid.com"
        else:
            # Fallback to sandbox for 'sandbox' or unknown
            host = plaid.Environment.Sandbox

        # Initialize Plaid client configuration
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
        """Check if the Plaid service has been configured with credentials."""
        return bool(self.client_id and self.secret)