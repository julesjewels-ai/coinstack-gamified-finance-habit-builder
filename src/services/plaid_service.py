import plaid
from plaid.api import plaid_api

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
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        # Determine the host based on the environment string
        if env.lower() == 'sandbox':
            host = plaid.Environment.Sandbox
        elif env.lower() == 'production':
            host = plaid.Environment.Production
        elif env.lower() == 'development':
            # plaid-python deprecated Development enum; use explicit URL
            host = 'https://development.plaid.com'
        else:
            host = plaid.Environment.Sandbox  # Default to sandbox if unrecognized

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
