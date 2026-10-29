import plaid
from plaid.api import plaid_api

from src.core.config import settings

class PlaidService:
    """
    Service for integrating with the Plaid API.
    Handles client initialization and API interactions.
    """
    def __init__(self) -> None:
        """
        Initializes the Plaid client using environment variables.
        """
        env = settings.PLAID_ENV.lower()
        if env == 'sandbox':
            host = plaid.Environment.Sandbox
        elif env == 'development':
            host = 'https://development.plaid.com'
        else:
            host = plaid.Environment.Production

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': settings.PLAID_CLIENT_ID,
                'secret': settings.PLAID_SECRET,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
