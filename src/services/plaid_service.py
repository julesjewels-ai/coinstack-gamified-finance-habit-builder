"""
Service for integrating with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from src.core.config import settings

class PlaidService:
    """
    Service class handling interactions with the Plaid API.
    """

    def __init__(self) -> None:
        """Initializes the Plaid client based on environment configuration."""
        self.client_id = settings.PLAID_CLIENT_ID
        self.secret = settings.PLAID_SECRET
        self.env_name = settings.PLAID_ENV.lower()

        if self.env_name == "production":
            host = plaid.Environment.Production
        elif self.env_name == "development":
            # Plaid SDK deprecated Development enum; use explicit host string.
            host = "https://development.plaid.com"
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
        self.client: plaid_api.PlaidApi = plaid_api.PlaidApi(api_client)
