"""
Service module for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles initialization and connection to Plaid environments.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()

        # Map the environment string to the appropriate Plaid Environment enum
        # Note: Plaid's development environment was deprecated, so we map
        # 'development' to 'sandbox' as a safe fallback for local dev.
        plaid_env = plaid.Environment.Sandbox
        if self.environment == "production":
            plaid_env = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the service is minimally configured (has credentials).

        Returns:
            bool: True if client_id and secret are present, False otherwise.
        """
        return bool(self.client_id) and bool(self.secret)
