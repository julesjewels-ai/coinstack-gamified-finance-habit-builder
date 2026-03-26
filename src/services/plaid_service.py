"""
Plaid API integration service for Coinstack.
Handles initialization and communication with Plaid API endpoints.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    A service class encapsulating the configuration and initialization
    of the Plaid API client.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with API credentials and sets up the Plaid client.

        Args:
            client_id (str): The Plaid API client ID.
            secret (str): The Plaid API secret.
            env (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Map environment string to Plaid Environment
        env_mapping = {
            "sandbox": plaid.Environment.Sandbox,
            "production": plaid.Environment.Production,
        }
        # Fallback to sandbox if environment is unrecognized
        host = env_mapping.get(self.env, plaid.Environment.Sandbox)

        self.configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        self.api_client = plaid.ApiClient(self.configuration)
        self.client = plaid_api.PlaidApi(self.api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client instance.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client.
        """
        return self.client
