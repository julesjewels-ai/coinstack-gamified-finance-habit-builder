import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for integrating with the Plaid API.
    Handles configuration and client initialization.
    """

    def __init__(self, client_id: str, secret: str, environment: str):
        """
        Initializes the Plaid client.

        Args:
            client_id (str): Plaid Client ID.
            secret (str): Plaid Secret.
            environment (str): Plaid Environment (e.g. 'sandbox', 'production', 'development').
        """
        self.client_id = client_id
        self.secret = secret

        # Note: the 'development' environment enum was deprecated in plaid-python
        if environment.lower() == 'production':
            host = plaid.Environment.Production
        else:
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
