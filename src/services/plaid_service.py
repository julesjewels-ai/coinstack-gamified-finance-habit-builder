"""
Plaid API integration service.
Handles connection and communication with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: Plaid client ID.
            secret: Plaid secret.
            environment: Plaid environment (sandbox, development, production).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        # Plaid environments mapping
        env_map = {
            "sandbox": plaid.Environment.Sandbox,
            "production": plaid.Environment.Production,
            "development": "https://development.plaid.com"
        }

        host = env_map.get(self.environment, plaid.Environment.Sandbox)

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
        Checks if the client has been configured with credentials.

        Returns:
            True if client_id and secret are provided, False otherwise.
        """
        return bool(self.client_id and self.secret)
