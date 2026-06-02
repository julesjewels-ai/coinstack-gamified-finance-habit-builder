"""
Service module for integrating with the Plaid API.
"""
import plaid
from plaid.api import plaid_api
from plaid.api_client import ApiClient
from plaid.configuration import Configuration

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
            env (str): The Plaid environment ('sandbox' or 'production'). 'development' will map to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map environment string to plaid.Environment
        if self.env_name in ['sandbox', 'development']:
            plaid_env = plaid.Environment.Sandbox
        elif self.env_name == 'production':
            plaid_env = plaid.Environment.Production
        else:
            raise ValueError(f"Invalid Plaid environment: {self.env_name}")

        configuration = Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        self.api_client = ApiClient(configuration)
        self.client = plaid_api.PlaidApi(self.api_client)
