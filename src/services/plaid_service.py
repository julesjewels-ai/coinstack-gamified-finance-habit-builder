import plaid
from plaid.api import plaid_api

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
        self.env = env.lower()

        # Map environment string to plaid.Environment
        plaid_env = plaid.Environment.Sandbox
        if self.env == 'production':
            plaid_env = plaid.Environment.Production
        elif self.env == 'sandbox':
            plaid_env = plaid.Environment.Sandbox
        else:
            # Default to Sandbox for any unrecognized or 'development' environment
            plaid_env = plaid.Environment.Sandbox

        # Configure Plaid client
        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
