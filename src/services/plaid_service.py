"""
Service for integrating with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Encapsulates interaction with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid client ID.
            secret: The Plaid secret.
            env: The Plaid environment ("sandbox", "development", or "production").
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Map env string to Plaid environment URLs
        host_map = {
            "sandbox": plaid.Environment.Sandbox,
            "development": "https://development.plaid.com",
            "production": plaid.Environment.Production
        }

        host = host_map.get(self.env, plaid.Environment.Sandbox)

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
        Returns True if the client has credentials (very basic check).
        """
        return bool(self.client_id and self.secret)
