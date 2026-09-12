import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    assert service.is_configured() is True
    # The plaid api client host should point to Sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="prod_id", secret="prod_secret", env="production")
    assert service.env == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="dev_id", secret="dev_secret", env="development")
    assert service.env == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_invalid_env():
    with pytest.raises(ValueError, match="Invalid Plaid environment"):
        PlaidService(client_id="test_id", secret="test_secret", env="invalid")

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
