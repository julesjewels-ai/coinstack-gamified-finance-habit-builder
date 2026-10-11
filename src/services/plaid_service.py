"""
Plaid API integration service.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api


class PlaidService:
    """Service to interact with the Plaid API."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Map environment string to plaid host
        if self.env == "sandbox":
            host = plaid.Environment.Sandbox
        elif self.env == "development":
            # plaid-python deprecated the Development enum, use direct URL
            host = "https://development.plaid.com"
        elif self.env == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox  # Default to sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
