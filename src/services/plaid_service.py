"""
Plaid service module.
Provides a service class for integrating with the Plaid API.
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
        Initializes the Plaid service.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment_str = environment.lower()

        if self.environment_str == "production":
            self.host = plaid.Environment.Production
        elif self.environment_str == "sandbox":
            self.host = plaid.Environment.Sandbox
        elif self.environment_str == "development":
            self.host = "https://development.plaid.com"
        else:
            # Default to sandbox if unknown
            self.host = plaid.Environment.Sandbox

        # Configure Plaid API client
        configuration = plaid.Configuration(
            host=self.host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid service is configured with credentials.

        Returns:
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id and self.secret)
