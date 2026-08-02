import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """Service for interacting with the Plaid API."""

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox"):
        """
        Initializes the PlaidService.

        Args:
            client_id (str): Plaid Client ID.
            secret (str): Plaid Secret.
            environment (str): Plaid environment ('sandbox' or 'production'). Defaults to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        self.client = self._create_client()

    def _create_client(self) -> plaid_api.PlaidApi:
        """Creates and returns the Plaid API client."""
        host = plaid.Environment.Sandbox
        # Plaid 'development' environment enum was deprecated, use Sandbox for non-production environments
        if self.environment.lower() == "production":
            host = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        client = plaid_api.PlaidApi(api_client)
        return client
