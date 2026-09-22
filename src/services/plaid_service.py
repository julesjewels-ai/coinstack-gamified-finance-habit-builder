"""
Service for integrating with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Encapsulates interaction with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment ('sandbox' or 'production'). Defaults to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        # Determine host based on environment
        if self.environment.lower() == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        # Initialize the Plaid API client
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
        Checks if the service has been configured with valid credentials.

        Returns:
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id and self.secret)
