"""
Service module for integrating with the Plaid API.
"""
import plaid
from plaid.api import plaid_api
import logging

logger = logging.getLogger(__name__)

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """

    def __init__(self, client_id: str, secret: str, env: str = "sandbox") -> None:
        """
        Initializes the PlaidService and configures the Plaid client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret.
            env (str): The Plaid environment (sandbox or production). Defaults to sandbox.
        """
        self.client_id = client_id
        self.secret = secret
        self.env = env

        host = plaid.Environment.Sandbox
        if self.env.lower() == "production":
            host = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
        logger.info(f"Plaid client initialized in {self.env} environment.")
