import pytest
from src.services.plaid_service import PlaidService
from src.core.app import App
import plaid

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.is_configured() is True
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.environment == "production"

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service.environment == "development"

def test_plaid_service_invalid_environment():
    with pytest.raises(ValueError):
        PlaidService(client_id="test_id", secret="test_secret", environment="invalid_env")

def test_app_initialization_with_injected_plaid_service():
    mock_service = PlaidService(client_id="mock_id", secret="mock_secret", environment="sandbox")
    app = App(debug_mode=True, plaid_service=mock_service)

    assert app.plaid_service is mock_service
    assert app.plaid_service.client_id == "mock_id"
