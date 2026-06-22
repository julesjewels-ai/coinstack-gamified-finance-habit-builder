"""
Plaid service module.
Handles integration with the Plaid API.
"""
import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment URL (e.g., plaid.Environment.Sandbox).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        configuration = plaid.Configuration(
            host=self.environment,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is configured properly.

        Returns:
            bool: True if properly configured with client_id and secret, False otherwise.
        """
        return bool(self.client_id and self.secret)
