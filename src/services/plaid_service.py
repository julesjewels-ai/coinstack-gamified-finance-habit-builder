import plaid
from plaid.api import plaid_api
from typing import Dict, Any

class PlaidService:
    """
    Service for interacting with the Plaid API.
    """
    def __init__(self, client_id: str, secret: str, environment: str) -> None:
        """
        Initializes the PlaidService.

        Args:
            client_id: Plaid client ID.
            secret: Plaid secret.
            environment: Plaid environment (e.g., 'sandbox', 'development', 'production').
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        # Mapping environment string to plaid environment host
        env_map = {
            "sandbox": plaid.Environment.Sandbox,
            "development": "https://development.plaid.com",
            "production": plaid.Environment.Production
        }

        host = env_map.get(environment.lower(), plaid.Environment.Sandbox)

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
