"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Encapsulates interactions with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id: The Plaid client ID.
            secret: The Plaid secret.
            env: The Plaid environment ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env.lower()

        # Determine correct host
        if self.env == "sandbox":
            host = plaid.Environment.Sandbox
        elif self.env == "development":
            # Plaid deprecated the Development enum, so we use the URL directly
            host = "https://development.plaid.com"
        elif self.env == "production":
            host = plaid.Environment.Production
        else:
            raise ValueError(f"Invalid Plaid environment: {self.env}")

        # Configure client
        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
