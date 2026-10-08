import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_init_sandbox() -> None:
    service = PlaidService(client_id="mock_id", secret="mock_secret", env="sandbox")
    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_init_development() -> None:
    service = PlaidService(client_id="mock_id", secret="mock_secret", env="development")
    assert service.client is not None
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_init_production() -> None:
    service = PlaidService(client_id="mock_id", secret="mock_secret", env="production")
    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_init_invalid_env() -> None:
    with pytest.raises(ValueError) as excinfo:
        PlaidService(client_id="mock_id", secret="mock_secret", env="invalid_env")
    assert "Invalid Plaid environment: invalid_env" in str(excinfo.value)
