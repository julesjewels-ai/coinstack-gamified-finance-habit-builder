"""
Plaid Service module for integrating with the Plaid API.
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
        Initializes the Plaid API client using the provided configuration.
        """
        # Determine the correct Plaid environment based on the configuration
        env_mapping = {
            "sandbox": plaid.Environment.Sandbox,
            "development": plaid.Environment.Sandbox,  # Deprecated in Plaid, map to Sandbox
            "production": plaid.Environment.Production
        }

        env_str = environment.lower()
        plaid_env = env_mapping.get(env_str, plaid.Environment.Sandbox)

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                "clientId": client_id,
                "secret": secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client instance.
        """
        return self.client
