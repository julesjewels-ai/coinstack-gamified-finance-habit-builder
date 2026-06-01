"""
Plaid service module for integrating with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment (e.g., 'sandbox', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_string = env.lower()

        # Map environment string to Plaid Environment enum
        # Note: The plaid-python library's Environment class only contains Sandbox and Production
        # Handle 'development' or anything else as Sandbox to be safe.
        if self.env_string == "production":
            plaid_env = plaid.Environment.Production
        else:
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
