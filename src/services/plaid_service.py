"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional
from src.core.config import settings


class PlaidService:
    """
    Service class to handle Plaid API initialization and interactions.
    """

    def __init__(self, client_id: Optional[str] = None, secret: Optional[str] = None, env: Optional[str] = None) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: Plaid client ID. Defaults to settings.PLAID_CLIENT_ID.
            secret: Plaid secret. Defaults to settings.PLAID_SECRET.
            env: Plaid environment. Defaults to settings.PLAID_ENV.
        """
        self.client_id: str = client_id if client_id is not None else settings.PLAID_CLIENT_ID
        self.secret: str = secret if secret is not None else settings.PLAID_SECRET
        self.env: str = (env if env is not None else settings.PLAID_ENV).lower()

        if self.env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env == 'production':
            host = plaid.Environment.Production
        elif self.env == 'development':
            # plaid-python deprecated the Development enum. Plaid recommends setting host explicitly.
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
        self.client: plaid_api.PlaidApi = plaid_api.PlaidApi(api_client)
