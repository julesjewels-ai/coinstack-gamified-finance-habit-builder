import plaid
from plaid.api import plaid_api

class PlaidService:
    """Service to interact with the Plaid API."""

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment_name = environment.lower()

        if self.environment_name == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.environment_name == 'production':
            host = plaid.Environment.Production
        elif self.environment_name == 'development':
            host = 'https://development.plaid.com'
        else:
            host = plaid.Environment.Sandbox # Default to sandbox

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
        """Checks if the service is properly configured."""
        return bool(self.client_id and self.secret)
