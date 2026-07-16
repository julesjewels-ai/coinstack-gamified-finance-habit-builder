import pytest
import plaid
from src.core.config import Settings
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'development' to Sandbox."""
    settings = Settings()
    settings.PLAID_CLIENT_ID = "test_client_id"
    settings.PLAID_SECRET = "test_secret"
    settings.PLAID_ENV = "development"

    service = PlaidService(settings)

    assert service.client is not None
    # Verify mapping fallback to Sandbox since development is deprecated
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' to Production."""
    settings = Settings()
    settings.PLAID_CLIENT_ID = "test_client_id"
    settings.PLAID_SECRET = "test_secret"
    settings.PLAID_ENV = "production"

    service = PlaidService(settings)

    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_credentials():
    """Test PlaidService properly parses credentials."""
    settings = Settings()
    settings.PLAID_CLIENT_ID = "test_client_id_123"
    settings.PLAID_SECRET = "test_secret_456"
    settings.PLAID_ENV = "sandbox"

    service = PlaidService(settings)

    config = service.client.api_client.configuration
    assert config.api_key['clientId'] == "test_client_id_123"
    assert config.api_key['secret'] == "test_secret_456"
