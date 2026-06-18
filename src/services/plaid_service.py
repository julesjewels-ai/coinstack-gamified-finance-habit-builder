"""
Plaid API Service integration.
Handles initialization and configuration of the Plaid client.
"""

import plaid
from plaid.api import plaid_api
from typing import Optional


class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client with the given credentials.

        Args:
            client_id (str): Plaid client ID.
            secret (str): Plaid secret.
            env (str): Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()
        self.client: Optional[plaid_api.PlaidApi] = None

        if self.client_id and self.secret:
            self._initialize_client()

    def _initialize_client(self) -> None:
        """
        Sets up the Plaid API client instance based on configuration.
        Maps the requested environment to Plaid's available environments.
        Note: The 'development' environment enum was deprecated in plaid-python,
        so configurations targeting 'development' map to Sandbox.
        """
        # Map environment to Plaid Environment
        if self.env == 'production':
            plaid_env = plaid.Environment.Production
        else:
            # Fallback for 'sandbox', 'development', or any other value
            plaid_env = plaid.Environment.Sandbox

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
        Checks if the Plaid client is properly initialized with credentials.

        Returns:
            bool: True if configured, False otherwise.
        """
        return self.client is not None
