"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class for Plaid integration.
    Handles initialization and interaction with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str = "sandbox") -> None:
        """
        Initializes the PlaidService with API credentials and environment.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
                       Defaults to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Map environment string to Plaid host
        if self.env == 'production':
            host = plaid.Environment.Production
        elif self.env == 'development':
            # plaid-python deprecated the Development enum, so we use the URL explicitly
            host = 'https://development.plaid.com'
        else:
            host = plaid.Environment.Sandbox

        # Initialize Plaid API Client
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
        Checks if the Plaid service has been configured with credentials.

        Returns:
            bool: True if client_id and secret are present, False otherwise.
        """
        return bool(self.client_id and self.secret)
