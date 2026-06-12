"""
Plaid API integration service.
Handles connecting to the Plaid API using the plaid-python client.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id: The Plaid API client ID.
            secret: The Plaid API secret.
            environment: The Plaid API environment (sandbox, development, production).
                         'development' is deprecated and maps to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = self._map_environment(environment)
        self.client = self._create_client()

    def _map_environment(self, environment_str: str) -> plaid.Environment:
        """
        Maps a string environment to the plaid.Environment enum.
        Handles the deprecated 'development' environment.
        """
        env_lower = environment_str.lower()
        if env_lower == "production":
            return plaid.Environment.Production
        # Treat both 'sandbox' and 'development' (deprecated) as Sandbox
        return plaid.Environment.Sandbox

    def _create_client(self) -> plaid_api.PlaidApi:
        """
        Creates and configures the Plaid API client.
        """
        configuration = plaid.Configuration(
            host=self.environment,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        return plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the service has been configured with credentials.
        """
        return bool(self.client_id and self.secret)
