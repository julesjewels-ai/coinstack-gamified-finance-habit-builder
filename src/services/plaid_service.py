"""
Plaid API Integration Service.
"""
from typing import Optional
import plaid
from plaid.api import plaid_api


class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The environment to run in ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()
        self.client: Optional[plaid_api.PlaidApi] = None
        self._initialize_client()

    def _initialize_client(self) -> None:
        """
        Sets up the internal Plaid ApiClient.
        """
        host = plaid.Environment.Sandbox
        if self.env_name == "production":
            host = plaid.Environment.Production
        elif self.env_name == "development":
            # Plaid deprecated the 'development' environment, map to sandbox for backward config compat.
            host = plaid.Environment.Sandbox
        elif self.env_name == "sandbox":
            host = plaid.Environment.Sandbox
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            },
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
