"""
Service for interacting with the Plaid API.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api
from plaid.model.country_code import CountryCode
from plaid.model.products import Products

class PlaidService:
    """
    Service class to encapsulate Plaid API communication.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id: The Plaid Client ID.
            secret: The Plaid Secret.
            env: The Plaid environment ('sandbox', 'development', 'production').
                 Note: 'development' is deprecated in the library and maps to sandbox.
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map environment string to Plaid Environment enum
        if self.env_name == 'production':
            plaid_env = plaid.Environment.Production
        else:
            # Map both 'sandbox' and 'development' (deprecated) to Sandbox
            plaid_env = plaid.Environment.Sandbox

        # Configure the Plaid client
        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Check if the Plaid client is properly configured with credentials.

        Returns:
            bool: True if both client_id and secret are provided, False otherwise.
        """
        return bool(self.client_id and self.secret)
