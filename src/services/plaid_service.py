"""
Plaid API Integration Service.
"""

import plaid
from plaid.api import plaid_api
import logging

logger = logging.getLogger(__name__)

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str = "sandbox") -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox' or 'production'). 'development' maps to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Handle deprecated development environment
        if self.env == "development":
            self.env = "sandbox"
            logger.warning("Plaid 'development' environment is deprecated. Mapping to 'sandbox'.")

        plaid_host = plaid.Environment.Production if self.env == "production" else plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=plaid_host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

        # Test connection by making a harmless request or just initializing successfully
        logger.info(f"Plaid client initialized for environment: {self.env}")

    def get_client(self) -> plaid_api.PlaidApi:
        """
        Returns the initialized PlaidApi client.

        Returns:
            plaid_api.PlaidApi: The Plaid API client.
        """
        return self.client
