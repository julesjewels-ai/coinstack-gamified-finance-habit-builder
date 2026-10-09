import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.client is not None
    assert service.is_configured() is True

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.environment == "production"
    assert service.client is not None

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service.environment == "development"
    assert service.client is not None

def test_plaid_service_invalid_environment():
    with pytest.raises(ValueError, match="Invalid Plaid environment: invalid_env"):
        PlaidService(client_id="test_id", secret="test_secret", environment="invalid_env")

def test_plaid_service_is_configured_false():
    service = PlaidService(client_id="", secret="", environment="sandbox")
    assert service.is_configured() is False

    service2 = PlaidService(client_id="id", secret="", environment="sandbox")
    assert service2.is_configured() is False
