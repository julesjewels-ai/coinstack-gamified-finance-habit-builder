"""
Plaid API integration service.
Handles initialization and connectivity with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class to encapsulate interactions with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        # Determine the host based on the environment string
        if env.lower() == 'sandbox':
            host = plaid.Environment.Sandbox
        elif env.lower() == 'production':
            host = plaid.Environment.Production
        elif env.lower() == 'development':
            # Plaid deprecated the Development enum; use the URL directly
            host = "https://development.plaid.com"
        else:
            raise ValueError(f"Invalid Plaid environment: {env}")

        # Configure the Plaid API client
        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        # Initialize the API client
        api_client = plaid.ApiClient(configuration)

        # Initialize the specific Plaid API implementation
        self.client = plaid_api.PlaidApi(api_client)

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized Plaid API client instance.

        Returns:
            plaid_api.PlaidApi: The configured Plaid API client.
        """
        return self.client
