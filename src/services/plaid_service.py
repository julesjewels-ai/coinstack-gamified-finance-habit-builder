import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_string = env.lower()

        # Map environment string to Plaid Environment enum
        # Note: 'development' is deprecated and maps to Sandbox.
        if self.env_string == 'production':
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

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is configured with credentials.
        """
        return bool(self.client_id) and bool(self.secret)
