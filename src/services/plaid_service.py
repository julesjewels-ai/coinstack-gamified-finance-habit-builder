import plaid
from plaid.api import plaid_api
import traceback

class PlaidService:
    """Service to interact with Plaid API."""

    def __init__(self, client_id: str, secret: str, environment: str):
        self.client_id = client_id
        self.secret = secret
        self.environment = environment

        try:
            if environment.lower() == 'sandbox':
                plaid_env = plaid.Environment.Sandbox
            elif environment.lower() == 'production':
                plaid_env = plaid.Environment.Production
            else:
                plaid_env = plaid.Environment.Sandbox # fallback

            configuration = plaid.Configuration(
                host=plaid_env,
                api_key={
                    'clientId': client_id,
                    'secret': secret,
                }
            )

            api_client = plaid.ApiClient(configuration)
            self.client = plaid_api.PlaidApi(api_client)
            self.connected = True
        except Exception as e:
            print(f"Error initializing Plaid client: {e}")
            traceback.print_exc()
            self.client = None
            self.connected = False

    def is_connected(self) -> bool:
        """Returns whether the Plaid client was successfully initialized."""
        return self.connected
