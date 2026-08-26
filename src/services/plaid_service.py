"""
Plaid API Client Integration
"""
import plaid
from plaid.api import plaid_api
from typing import Optional


class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str = "sandbox"):
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid Client ID.
            secret: The Plaid Secret.
            env: The Plaid environment ('sandbox' or 'production'). Defaults to 'sandbox'.
                 Note: 'development' is mapped to Sandbox per SDK updates.
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Plaid's SDK currently supports Sandbox and Production.
        if self.env_name == "production":
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

    def get_client(self) -> plaid_api.PlaidApi:
        """Returns the initialized Plaid API client."""
        return self.client
