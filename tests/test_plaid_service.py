import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_sandbox_mapping():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.client_id == "test_id"

def test_plaid_service_development_mapping():
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_production_mapping():
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_invalid_env():
    with pytest.raises(ValueError, match="Invalid Plaid environment: invalid_env"):
        PlaidService(client_id="test_id", secret="test_secret", env="invalid_env")
