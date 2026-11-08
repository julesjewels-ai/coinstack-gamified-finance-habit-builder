"""
Plaid API integration service.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api
from src.core.config import settings

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(
        self,
        client_id: Optional[str] = None,
        secret: Optional[str] = None,
        env: Optional[str] = None
    ) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (Optional[str]): Plaid Client ID. Defaults to settings.PLAID_CLIENT_ID.
            secret (Optional[str]): Plaid Secret. Defaults to settings.PLAID_SECRET.
            env (Optional[str]): Plaid Environment ('sandbox', 'development', 'production').
                Defaults to settings.PLAID_ENV.
        """
        self.client_id = client_id if client_id is not None else settings.PLAID_CLIENT_ID
        self.secret = secret if secret is not None else settings.PLAID_SECRET
        self.env = env if env is not None else settings.PLAID_ENV

        self.client = self._create_client()

    def _create_client(self) -> plaid_api.PlaidApi:
        """
        Creates and returns the Plaid API client instance.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client.
        """
        host = plaid.Environment.Sandbox
        if self.env.lower() == 'production':
            host = plaid.Environment.Production
        elif self.env.lower() == 'development':
            host = 'https://development.plaid.com'

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        return plaid_api.PlaidApi(api_client)
