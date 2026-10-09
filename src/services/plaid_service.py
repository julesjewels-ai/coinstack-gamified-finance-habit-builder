import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles initialization and core functionality like token exchange and data retrieval.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        # Plaid SDK requires 'clientId' and 'secret' mapping
        api_keys = {
            'clientId': self.client_id,
            'secret': self.secret,
        }

        # Resolve host based on environment string
        if self.environment == 'production':
            host = plaid.Environment.Production
        elif self.environment == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.environment == 'development':
            # Plaid deprecated the Development environment enum in newer SDKs, so use the URL
            host = 'https://development.plaid.com'
        else:
            raise ValueError(f"Invalid Plaid environment: {self.environment}")

        configuration = plaid.Configuration(
            host=host,
            api_key=api_keys,
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client has been configured with credentials.

        Returns:
            bool: True if client ID and secret are set, False otherwise.
        """
        return bool(self.client_id and self.secret)
