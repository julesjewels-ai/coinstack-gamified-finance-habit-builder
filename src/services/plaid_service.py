"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api


class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env

        if env.lower() == "sandbox":
            host = plaid.Environment.Sandbox
        elif env.lower() == "production":
            host = plaid.Environment.Production
        elif env.lower() == "development":
            host = "https://development.plaid.com"
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                "clientId": client_id,
                "secret": secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is properly configured with credentials.

        Returns:
            bool: True if client ID and secret are set, False otherwise.
        """
        return bool(self.client_id and self.secret)
