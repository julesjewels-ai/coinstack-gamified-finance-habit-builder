"""
Service for interacting with the Plaid API.
"""

import plaid
from plaid.api import plaid_api

from typing import Optional, Dict, Any, List

class PlaidService:
    """
    Encapsulates Plaid API setup and interactions.
    """

    def __init__(
        self,
        client_id: str,
        secret: str,
        environment: str = "sandbox"
    ) -> None:
        """
        Initializes the Plaid client.

        Args:
            client_id (str): The Plaid client ID.
            secret (str): The Plaid secret.
            environment (str): The Plaid environment (sandbox or production).
        """
        # Define environment based on string
        if environment.lower() == "production":
            plaid_env = plaid.Environment.Production
        else:
             # Default to sandbox and map deprecated 'development' to sandbox as well per memory constraints
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
