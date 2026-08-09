"""
Plaid API integration service.
Handles initialization and communication with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles environment configuration and client initialization.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the PlaidService and underlying Plaid API client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The environment to connect to ('sandbox' or 'production').
                Defaults to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()
        self.client: Optional[plaid_api.PlaidApi] = None

        self._initialize_client()

    def _initialize_client(self) -> None:
        """
        Sets up the Plaid API client using the provided configuration.
        """
        if self.environment == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is properly initialized with credentials.

        Returns:
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id and self.secret and self.client)
