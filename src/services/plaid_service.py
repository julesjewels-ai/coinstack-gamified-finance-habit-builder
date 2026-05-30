"""
Plaid API integration service.
Handles initialization and communication with the Plaid API.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map string environment to Plaid environment object
        if self.env_name == 'sandbox':
            self.plaid_env = plaid.Environment.Sandbox
        elif self.env_name == 'production':
            self.plaid_env = plaid.Environment.Production
        else:
            # Fallback to sandbox if invalid or 'development' (deprecated)
            print(f"Warning: Unknown or deprecated Plaid environment '{env}'. Defaulting to Sandbox.")
            self.plaid_env = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=self.plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
