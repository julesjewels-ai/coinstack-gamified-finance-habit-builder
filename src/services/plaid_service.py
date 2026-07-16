import plaid
from plaid.api import plaid_api
from src.core.config import Settings

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    Handles configuration, initialization, and connection to Plaid environments.
    """

    def __init__(self, settings: Settings) -> None:
        """
        Initializes the PlaidService with the provided application settings.

        Args:
            settings (Settings): The application settings object injected for dependency inversion.
        """
        self.settings = settings

        # Map environment string to plaid Environment. 'development' maps to Sandbox as per deprecation.
        env_lower = self.settings.PLAID_ENV.lower()
        if env_lower == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.settings.PLAID_CLIENT_ID,
                'secret': self.settings.PLAID_SECRET,
            }
        )

        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
