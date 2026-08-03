import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env_string == "sandbox"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_initialization_development():
    # 'development' should map to Sandbox
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env_string == "development"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.env_string == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
