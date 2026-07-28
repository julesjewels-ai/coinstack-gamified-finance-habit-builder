"""
Service for integrating with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class to handle Plaid API interactions.
    """

    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initialize the Plaid API client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            environment (str): The Plaid environment ('sandbox' or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        # Plaid's SDK environment handling
        if environment.lower() in ['production', 'prod']:
            plaid_env = plaid.Environment.Production
        else:
            # Map 'development', 'sandbox', or anything else to Sandbox
            plaid_env = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=plaid_env,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Check if the Plaid service has been configured with credentials.
        """
        return bool(self.client_id and self.secret)
