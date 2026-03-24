import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox"):
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment to connect to (sandbox, production).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        # Determine the Plaid environment URL based on the provided environment string
        if self.environment.lower() == "sandbox":
            plaid_env = plaid.Environment.Sandbox
        elif self.environment.lower() == "production":
            plaid_env = plaid.Environment.Production
        else:
            raise ValueError(f"Invalid Plaid environment: {self.environment}")

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid service has been configured with credentials.

        Returns:
            bool: True if client_id and secret are present, False otherwise.
        """
        return bool(self.client_id and self.secret)
