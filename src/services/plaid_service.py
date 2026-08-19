"""
Service for integrating with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class to handle Plaid API initialization and basic connection testing.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id: The Plaid Client ID.
            secret: The Plaid Secret.
            env: The Plaid environment ('sandbox' or 'production').
                 'development' is mapped to 'sandbox' as it is deprecated.
        """
        self.client_id = client_id
        self.secret = secret

        # Determine the correct Plaid environment
        plaid_env = plaid.Environment.Sandbox
        env_lower = env.lower()
        if env_lower == 'production':
            plaid_env = plaid.Environment.Production
        elif env_lower == 'development':
             # The development environment is deprecated, map to Sandbox
             plaid_env = plaid.Environment.Sandbox

        # Initialize the Plaid API Client
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
        Checks if the service has been configured with credentials.

        Returns:
            bool: True if client_id and secret are provided, False otherwise.
        """
        return bool(self.client_id and self.secret)
