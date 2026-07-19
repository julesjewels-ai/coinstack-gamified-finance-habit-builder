import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for integrating with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env_name: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid Client ID.
            secret: The Plaid Secret for the target environment.
            env_name: The Plaid environment name (e.g., 'sandbox', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env_name.lower()

        # Map environment string to Plaid Environment
        host = plaid.Environment.Sandbox
        if self.env_name == 'production':
            host = plaid.Environment.Production

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
