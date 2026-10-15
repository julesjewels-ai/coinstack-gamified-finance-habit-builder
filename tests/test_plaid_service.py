import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_sandbox() -> None:
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.client is not None

def test_plaid_service_development() -> None:
    service = PlaidService(client_id="test_client", secret="test_secret", environment="development")
    assert service.environment == "development"
    assert service.client is not None

def test_plaid_service_production() -> None:
    service = PlaidService(client_id="test_client", secret="test_secret", environment="production")
    assert service.environment == "production"
    assert service.client is not None

def test_plaid_service_invalid_environment() -> None:
    with pytest.raises(ValueError, match="Invalid Plaid environment: invalid"):
        PlaidService(client_id="test_client", secret="test_secret", environment="invalid")
