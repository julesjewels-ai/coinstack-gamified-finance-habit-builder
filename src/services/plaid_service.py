import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for integrating with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str):
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        if self.environment == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.environment == 'production':
            host = plaid.Environment.Production
        elif self.environment == 'development':
            host = 'https://development.plaid.com'
        else:
            raise ValueError(f"Invalid Plaid environment: {self.environment}")

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Returns True if the client is configured with credentials.
        """
        return bool(self.client_id and self.secret)
