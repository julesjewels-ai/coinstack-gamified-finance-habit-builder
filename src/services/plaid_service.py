import plaid
from plaid.api import plaid_api
from typing import Optional

class PlaidService:
    """
    Service for integrating with the Plaid API.
    Handles configuration and API client setup for bank connectivity.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id (str): Plaid client ID.
            secret (str): Plaid secret.
            env (str): Plaid environment ('sandbox' or 'production').
                       'development' is mapped to 'sandbox'.
        """
        self.client_id = client_id
        self.secret = secret

        # Map environment to Plaid's expected values
        if env.lower() == "production":
            self.plaid_env = plaid.Environment.Production
        else:
            # Fallback to Sandbox for anything else (including 'development' which is deprecated)
            self.plaid_env = plaid.Environment.Sandbox

        self.configuration = plaid.Configuration(
            host=self.plaid_env,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        self.api_client = plaid.ApiClient(self.configuration)
        self.client = plaid_api.PlaidApi(self.api_client)

    def is_configured(self) -> bool:
        """Checks if the service has been configured with credentials."""
        return bool(self.client_id and self.secret)
