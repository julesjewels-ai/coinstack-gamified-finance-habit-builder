"""
Service module for integrating with the Plaid API.
"""

from typing import Optional, Dict, Any
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

class PlaidService:
    """
    Service class for Plaid API integration.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initialize the Plaid service.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            env (str): The Plaid environment ('sandbox', 'development', or 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        if self.env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif self.env == 'development':
            # Plaid-python deprecated Development enum, explicitly use URL
            host = 'https://development.plaid.com'
        elif self.env == 'production':
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox # Default to sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def create_link_token(self, client_user_id: str) -> Optional[str]:
        """
        Create a link token for the Plaid Link flow.

        Args:
            client_user_id (str): The unique ID of the user in our system.

        Returns:
            Optional[str]: The link token if successful, None otherwise.
        """
        try:
            request = LinkTokenCreateRequest(
                products=[Products('transactions')],
                client_name="Coinstack Gamified Finance",
                country_codes=[CountryCode('US')],
                language='en',
                user=LinkTokenCreateRequestUser(
                    client_user_id=client_user_id
                )
            )
            response = self.client.link_token_create(request)
            return response['link_token']
        except Exception as e:
            print(f"Error creating link token: {e}")
            return None
