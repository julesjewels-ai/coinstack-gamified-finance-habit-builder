"""
Plaid API integration service.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class to handle Plaid API connectivity and operations.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the Plaid Service.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret for the given environment.
            environment (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()
        self.client: Optional[plaid_api.PlaidApi] = None
        self._initialize_client()

    def _initialize_client(self) -> None:
        """
        Initializes the Plaid API client based on the provided configuration.
        """
        if not self.client_id or not self.secret:
            raise ValueError("Plaid Client ID and Secret are required.")

        if self.environment == "production":
            host = plaid.Environment.Production
        elif self.environment == "development":
            # plaid-python deprecated Development enum
            host = "https://development.plaid.com"
        else:
            host = plaid.Environment.Sandbox

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
        """
        Checks if the Plaid client is fully configured and ready.

        Returns:
            bool: True if configured correctly, False otherwise.
        """
        return self.client is not None
