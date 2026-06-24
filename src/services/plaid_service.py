import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment (e.g., 'sandbox', 'production').
        """
        if environment.lower() in ("sandbox", "development"):
            host = plaid.Environment.Sandbox
        elif environment.lower() == "production":
            host = plaid.Environment.Production
        else:
            raise ValueError(f"Unsupported Plaid environment: {environment}")

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client.
        """
        return self.client
