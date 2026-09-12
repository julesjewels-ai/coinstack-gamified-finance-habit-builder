import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles configuration and client initialization.
    """
    def __init__(self, client_id: str, secret: str, env: str = "sandbox") -> None:
        """
        Initializes the Plaid service with the given credentials.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        host = plaid.Environment.Sandbox
        if self.env == "development":
            host = "https://development.plaid.com"
        elif self.env == "production":
            host = plaid.Environment.Production
        elif self.env == "sandbox":
            host = plaid.Environment.Sandbox
        else:
            raise ValueError(f"Invalid Plaid environment: {self.env}")

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
        """Returns True if the client is configured with credentials."""
        return bool(self.client_id and self.secret)
