from src.services.plaid_service import PlaidService
import plaid

class MockSettings:
    def __init__(self):
        self.PLAID_CLIENT_ID = "test_client_id"
        self.PLAID_SECRET = "test_secret"
        self.PLAID_ENV = "sandbox"

class MockProductionSettings:
    def __init__(self):
        self.PLAID_CLIENT_ID = "test_client_id"
        self.PLAID_SECRET = "test_secret"
        self.PLAID_ENV = "production"

def test_plaid_service_initialization_sandbox():
    settings = MockSettings()
    service = PlaidService(settings)

    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"

    client = service.get_client()
    assert client is not None

def test_plaid_service_initialization_production():
    settings = MockProductionSettings()
    service = PlaidService(settings)

    assert service.env == "production"
    assert service.get_client() is not None
