import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """
    def __init__(self, client_id: str, secret: str, env: str = "sandbox"):
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment (sandbox, production, etc).
                       If 'development' is provided, it maps to Sandbox.
        """
        self.client_id = client_id
        self.secret = secret

        env_lower = env.lower()
        if env_lower == "development" or env_lower == "sandbox":
            plaid_env = plaid.Environment.Sandbox
        elif env_lower == "production":
            plaid_env = plaid.Environment.Production
        else:
            plaid_env = plaid.Environment.Sandbox # Default to sandbox

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
        Returns True if the client is configured with both a client_id and a secret.
        """
        return bool(self.client_id) and bool(self.secret)
