"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from src.core.config import Settings

class PlaidService:
    """
    A service class that wraps the Plaid API client and provides methods
    for connecting to banks, fetching transactions, etc.
    """

    def __init__(self, settings: Settings) -> None:
        """
        Initializes the PlaidService and configures the Plaid client.

        Args:
            settings (Settings): The application settings object containing
                the necessary Plaid credentials.
        """
        # Determine the Plaid environment.
        # Plaid SDK primarily uses Sandbox and Production.
        env_str = settings.PLAID_ENV.lower()
        if env_str == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': settings.PLAID_CLIENT_ID,
                'secret': settings.PLAID_SECRET,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
