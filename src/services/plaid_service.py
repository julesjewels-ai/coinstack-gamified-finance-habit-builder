"""
Plaid API Integration Service.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api


class PlaidService:
    """
    Service for integrating with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment (sandbox, development, or production).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment
        self.client = self._initialize_client()

    def _get_plaid_environment(self) -> plaid.Environment:
        """
        Maps the string environment to the plaid.Environment enum.

        Returns:
            plaid.Environment: The corresponding Plaid environment.
        """
        env_lower = self.environment.lower()
        if env_lower == "production":
            return plaid.Environment.Production
        # Plaid SDK doesn't have Development, map development/sandbox to Sandbox
        return plaid.Environment.Sandbox

    def _initialize_client(self) -> plaid_api.PlaidApi:
        """
        Initializes and returns the Plaid API client.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client.
        """
        configuration = plaid.Configuration(
            host=self._get_plaid_environment(),
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        return plaid_api.PlaidApi(api_client)
