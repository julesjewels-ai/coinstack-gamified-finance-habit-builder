"""
Plaid service module for interacting with the Plaid API.
"""
import plaid
from plaid.api import plaid_api

class PlaidService:
    """Service class to handle Plaid API interactions."""

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env
        self.client = self._initialize_client()

    def _initialize_client(self) -> plaid_api.PlaidApi:
        """
        Initializes and returns the Plaid API client.

        Returns:
            plaid_api.PlaidApi: The initialized Plaid client.
        """
        env_map = {
            'sandbox': plaid.Environment.Sandbox,
            'development': plaid.Environment.Sandbox,
            'production': plaid.Environment.Production,
        }

        environment = env_map.get(self.env.lower(), plaid.Environment.Sandbox)

        configuration = plaid.Configuration(
            host=environment,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        return plaid_api.PlaidApi(api_client)
