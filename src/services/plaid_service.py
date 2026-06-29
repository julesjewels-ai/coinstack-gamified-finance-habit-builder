"""
Plaid API integration service.
"""

import plaid
from plaid.api import plaid_api
from plaid.model.country_code import CountryCode
from plaid.model.products import Products

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, environment: str = "sandbox") -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment (sandbox or production). Defaults to sandbox.
        """
        if environment.lower() == "production":
            host = plaid.Environment.Production
        else:
            # Map everything else (including 'development' which is deprecated) to Sandbox
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': client_id,
                'secret': secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """
        Checks if the Plaid client is properly configured.

        Returns:
            bool: True if configured, False otherwise.
        """
        # A simple check to see if we have credentials set up in the configuration
        return bool(self.client.api_client.configuration.api_key.get('clientId'))
