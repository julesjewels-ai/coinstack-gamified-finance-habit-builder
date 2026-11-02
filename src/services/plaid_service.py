"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str = "sandbox") -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Determine host based on env string
        if self.env == 'production':
            host = plaid.Environment.Production
        elif self.env == 'development':
            # Plaid SDK deprecated Development enum, explicitly use string for Development
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
