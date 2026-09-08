import plaid
from plaid.api import plaid_api

class PlaidService:
    """
    Service class for interacting with the Plaid API.
    """
    def __init__(self, client_id: str, secret: str, env: str = "sandbox"):
        self.client_id = client_id
        self.secret = secret
        self.env_name = env.lower()

        if self.env_name == "production":
            host = plaid.Environment.Production
        else:
            host = plaid.Environment.Sandbox

        configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': self.client_id,
                'secret': self.secret,
            }
        )
        api_client = plaid.ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
