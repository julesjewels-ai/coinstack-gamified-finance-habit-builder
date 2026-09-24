import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    # Ensure the configuration host points to sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    # Ensure the configuration host points to development custom string
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    # Ensure the configuration host points to production
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_invalid_env():
    with pytest.raises(ValueError, match="Invalid Plaid environment"):
        PlaidService(client_id="test_id", secret="test_secret", env="invalid")
