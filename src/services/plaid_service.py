"""
Plaid service module.
Handles initialization and configuration of the Plaid API client.
"""

from typing import Optional
import plaid
from plaid.api import plaid_api
import logging

logger = logging.getLogger(__name__)

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles client setup using environment variables.
    """

    def __init__(self, client_id: str, secret: str, env: str) -> None:
        """
        Initializes the PlaidService and sets up the API client.

        Args:
            client_id (str): The Plaid Client ID.
            secret (str): The Plaid Secret key.
            env (str): The environment to connect to ('sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()
        self.client: Optional[plaid_api.PlaidApi] = None

        self._initialize_client()

    def _get_plaid_environment(self) -> str:
        """
        Resolves the Plaid environment host string based on the env_name.

        Returns:
            str: The Plaid environment host URL.
        """
        if self.env_name == 'sandbox':
            return plaid.Environment.Sandbox
        elif self.env_name == 'production':
            return plaid.Environment.Production
        elif self.env_name == 'development':
            # Plaid deprecated the Development enum, so we explicitly return the URL
            return 'https://development.plaid.com'
        else:
            logger.warning(f"Unknown Plaid environment '{self.env_name}', falling back to sandbox.")
            return plaid.Environment.Sandbox

    def _initialize_client(self) -> None:
        """
        Initializes the internal PlaidApi client using the provided configuration.
        """
        try:
            host = self._get_plaid_environment()

            configuration = plaid.Configuration(
                host=host,
                api_key={
                    'clientId': self.client_id,
                    'secret': self.secret,
                }
            )

            api_client = plaid.ApiClient(configuration)
            self.client = plaid_api.PlaidApi(api_client)
            logger.info(f"Successfully initialized Plaid client for environment: {self.env_name}")

        except Exception as e:
            logger.error(f"Failed to initialize Plaid client: {e}")
            raise
