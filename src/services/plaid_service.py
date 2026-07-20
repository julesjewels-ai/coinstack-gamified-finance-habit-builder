"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class encapsulating the Plaid API client.
    """

    def __init__(self, client_id: str, secret: str, env: str = "sandbox") -> None:
        """
        Initialize the Plaid API client.

        Args:
            client_id (str): Plaid client ID.
            secret (str): Plaid secret.
            env (str): Plaid environment ('sandbox' or 'production'). Defaults to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Determine the Plaid environment
        if self.env_name == "production":
            plaid_env = plaid.Environment.Production
        else:
            # Map development or anything else to sandbox due to development being deprecated
            plaid_env = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
