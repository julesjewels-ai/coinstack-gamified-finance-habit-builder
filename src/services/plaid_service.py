"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """Service class for interacting with the Plaid API."""

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        host = plaid.Environment.Sandbox
        if environment == "development":
            host = "https://development.plaid.com"
        elif environment == "production":
            host = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """Check if Plaid service is configured with credentials."""
        return bool(self.client_id) and bool(self.secret)
