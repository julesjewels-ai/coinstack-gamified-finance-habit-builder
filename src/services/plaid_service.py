from typing import Any
import plaid
from plaid.api import plaid_api
from src.core.config import settings

class PlaidService:
    """Service class for interacting with the Plaid API."""
    def __init__(self) -> None:
        """Initializes the PlaidService by loading configuration and creating the API client."""
        self.client_id = settings.PLAID_CLIENT_ID
        self.secret = settings.PLAID_SECRET
        self.env = settings.PLAID_ENV

        self.host = plaid.Environment.Sandbox
        if self.env.lower() == "development":
            self.host = "https://development.plaid.com"
        elif self.env.lower() == "production":
            self.host = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=self.host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the required Plaid credentials have been configured.

        Returns:
            bool: True if both client ID and secret are present, False otherwise.
        """
        return bool(self.client_id and self.secret)
