import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service wrapper for the Plaid API client.
    Handles configuration, environment mapping, and initialization.
    """
    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with the provided credentials and environment.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The environment string (e.g., 'sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        # Map string environment to Plaid Environment
        if self.env_name == 'sandbox' or self.env_name == 'development':
            plaid_env = plaid.Environment.Sandbox
        elif self.env_name == 'production':
            plaid_env = plaid.Environment.Production
        else:
            plaid_env = plaid.Environment.Sandbox # fallback

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client instance.
        """
        return self.client
