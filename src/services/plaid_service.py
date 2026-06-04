"""
Plaid service module.
Provides an integration service with the Plaid API using the plaid-python client.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    A service class encapsulating the Plaid API client.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The environment to connect to ('sandbox' or 'production'). 'development' maps to 'sandbox'.
        """
        # Map environment string to Plaid Environment constants.
        env_lower = env.lower()
        if env_lower in ("sandbox", "development"):
            plaid_env = plaid.Environment.Sandbox
        elif env_lower == "production":
            plaid_env = plaid.Environment.Production
        else:
            # Default to sandbox if unknown
            plaid_env = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
