"""
Plaid API integration service.
"""

from typing import Dict, Optional, Any
import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class to interact with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initialize the Plaid API client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        # plaid-python deprecated Development enum, so we handle it explicitly
        if self.environment == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.environment == 'production':
            host = plaid.Environment.Production
        elif self.environment == 'development':
            host = 'https://development.plaid.com'
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
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Check if the Plaid client has been configured with credentials.

        Returns:
            bool: True if configured, False otherwise.
        """
        return bool(self.client_id and self.secret)
