"""
Service module for handling Plaid API interactions.
"""

import plaid
from plaid.api import plaid_api
import warnings

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles configuration and client initialization.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Plaid-python deprecated Development enum, explicitly set the host
        if self.env == 'development':
            host = 'https://development.plaid.com'
        elif self.env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env == 'production':
            host = plaid.Environment.Production
        else:
            warnings.warn(f"Unknown Plaid environment '{self.env}'. Defaulting to Sandbox.")
            host = plaid.Environment.Sandbox

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
        Checks if the client ID and secret are set.

        Returns:
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id and self.secret)
