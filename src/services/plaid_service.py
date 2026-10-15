import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service for integrating with the Plaid API.
    Handles client initialization and API interactions.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the PlaidService with API credentials.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()
        self.client: Optional[plaid_api.PlaidApi] = None

        self._initialize_client()

    def _initialize_client(self) -> None:
        """
        Initializes the Plaid API client using the provided credentials.
        """
        host = plaid.Environment.Sandbox

        if self.environment == "development":
            host = "https://development.plaid.com"
        elif self.environment == "production":
            host = plaid.Environment.Production
        elif self.environment == "sandbox":
            host = plaid.Environment.Sandbox
        else:
             raise ValueError(f"Invalid Plaid environment: {self.environment}")

        configuration = plaid.Configuration(
            host=host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
