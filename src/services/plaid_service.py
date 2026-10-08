import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService with the provided credentials.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment (sandbox, development, or production).

        Raises:
            ValueError: If an invalid environment is provided.
        """
        env_lower = env.lower()
        if env_lower == "sandbox":
            host = plaid.Environment.Sandbox
        elif env_lower == "production":
            host = plaid.Environment.Production
        elif env_lower == "development":
            # Plaid SDK deprecated the Development enum, so we manually set the URL
            host = "https://development.plaid.com"
        else:
            raise ValueError(f"Invalid Plaid environment: {env}")

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
