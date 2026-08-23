import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService and sets up the Plaid API client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox' or 'production').
                'development' will be mapped to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret

        # Map development environment to sandbox as development was deprecated
        if environment.lower() in ['sandbox', 'development']:
            host = plaid.Environment.Sandbox
        elif environment.lower() == 'production':
            host = plaid.Environment.Production
        else:
            # Default to Sandbox if not recognized, ensuring safety
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
