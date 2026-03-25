"""
Service for integrating with the Plaid API.
"""
import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.

    Initializes the plaid-python client based on configuration settings.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService and configures the Plaid client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The environment to run the Plaid API in (sandbox, development, production).
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Determine the correct Plaid environment
        if self.env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env == 'development':
            host = plaid.Environment.Development
        elif self.env == 'production':
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
        self.connected = False

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the configured Plaid client instance.
        """
        return self.client
