"""
Plaid API Integration Service.
"""
from typing import Optional
import plaid
from plaid.api import plaid_api
from src.core.config import settings

class PlaidService:
    """Service to interact with the Plaid API."""
    def __init__(self, client_id: Optional[str] = None, secret: Optional[str] = None, env: Optional[str] = None) -> None:
        self.client_id = client_id or settings.PLAID_CLIENT_ID
        self.secret = secret or settings.PLAID_SECRET
        self.env_name = (env or settings.PLAID_ENV).lower()

        if self.env_name == "sandbox":
            host = plaid.Environment.Sandbox
        elif self.env_name == "development":
            host = "https://development.plaid.com"
        elif self.env_name == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox # fallback

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)

    def is_configured(self) -> bool:
        """Check if basic credentials are provided."""
        return bool(self.client_id and self.secret)
