"""
Plaid API Service Integration.
Handles communication with the Plaid API for bank connections.
"""

import plaid
from plaid.api import plaid_api
from typing import Dict, Any


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
            environment (str): The Plaid environment (sandbox, production).
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment.lower()
        self.client = self._initialize_client()

    def _initialize_client(self) -> plaid_api.PlaidApi:
        """
        Sets up the Plaid API client configuration.
        Maps the environment string to the corresponding Plaid Environment Enum.
        """
        # Map environment string to Plaid Environment
        env_mapping: Dict[str, plaid.Environment] = {
            "sandbox": plaid.Environment.Sandbox,
            "development": plaid.Environment.Sandbox, # 'development' was deprecated
            "production": plaid.Environment.Production,
        }

        # Default to sandbox if the environment is not recognized
        host = env_mapping.get(self.environment, plaid.Environment.Sandbox)

        configuration = plaid.Configuration(
            host=host,
            api_key={
                "clientId": self.client_id,
                "secret": self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        return plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the service has been configured with credentials.
        """
        return bool(self.client_id and self.secret)
