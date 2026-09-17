"""
Service class for interacting with the Plaid API.
"""
from typing import Optional
import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    A service class encapsulating logic for Plaid API interactions.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment (sandbox, development, production).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        # Determine Plaid Host
        if self.environment == "sandbox":
            self.host = plaid.Environment.Sandbox
        elif self.environment == "development":
            self.host = "https://development.plaid.com"
        elif self.environment == "production":
            self.host = plaid.Environment.Production
        else:
            # Fallback to sandbox if not matched
            self.host = plaid.Environment.Sandbox

        self._initialize_client()

    def _initialize_client(self) -> None:
        """Initializes the Plaid API client."""
        configuration = plaid.Configuration(
            host=self.host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
