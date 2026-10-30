"""
Plaid API integration service.
Handles initialization of the Plaid client and interactions with the Plaid API.
"""
import plaid
from plaid.api import plaid_api


class PlaidService:
    """Service class for interacting with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initialize the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret for the specified environment.
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        host = plaid.Environment.Sandbox
        if self.env == "development":
            host = "https://development.plaid.com"
        elif self.env == "production":
            host = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Return the configured Plaid API client.

        Returns:
            plaid_api.PlaidApi: The Plaid API client.
        """
        return self.client
