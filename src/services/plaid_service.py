"""
Plaid API integration service.
Handles connecting to Plaid environments and making API requests.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api

class PlaidService:
    """Service to interact with the Plaid API."""

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The target Plaid environment (sandbox, development, production).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        self.host = self._get_host_for_environment(self.environment)
        self.client = self._initialize_client()

    def _get_host_for_environment(self, environment: str) -> str:
        """Returns the appropriate Plaid API host URL for the given environment."""
        if environment == "production":
            return plaid.Environment.Production
        elif environment == "sandbox":
            return plaid.Environment.Sandbox
        elif environment == "development":
            # Plaid-python deprecated the Development enum, so we explicitly set the host
            return "https://development.plaid.com"
        else:
            # Fallback to sandbox
            return plaid.Environment.Sandbox

    def _initialize_client(self) -> plaid_api.PlaidApi:
        """Initializes the plaid_api.PlaidApi client using the provided credentials."""
        configuration = plaid.Configuration(
            host=self.host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        return plaid_api.PlaidApi(api_client)
