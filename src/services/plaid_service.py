"""
Plaid service module.
Encapsulates Plaid API client initialization and interactions.
"""

import plaid
from plaid.api import plaid_api
from src.core.config import settings

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self) -> None:
        """
        Initializes the Plaid client.
        Raises ValueError if environment is unknown.
        """
        self.env = settings.PLAID_ENV.lower()

        # Determine Plaid API host
        if self.env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env == 'development':
            # plaid-python deprecated Development enum, must explicitly set
            host = 'https://development.plaid.com'
        elif self.env == 'production':
            host = plaid.Environment.Production
        else:
            raise ValueError(f"Unknown Plaid environment: {self.env}")

        # Initialize configuration
        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': settings.PLAID_CLIENT_ID,
                'secret': settings.PLAID_SECRET,
            }
        )

        # Initialize API client
        api_client = plaid.ApiClient(configuration)

        # Initialize Plaid API
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the client ID and secret are configured.
        """
        return bool(settings.PLAID_CLIENT_ID and settings.PLAID_SECRET)
