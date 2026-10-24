import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    # ApiClient config host should map to Sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_development():
    service = PlaidService(client_id="dev_id", secret="dev_secret", env="development")
    assert service.env == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"
    assert service.is_configured() is True

def test_plaid_service_production():
    service = PlaidService(client_id="prod_id", secret="prod_secret", env="production")
    assert service.env == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production
    assert service.is_configured() is True

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False

def test_plaid_service_case_insensitive_env():
    service = PlaidService(client_id="id", secret="secret", env="SANDBOX")
    assert service.env == "sandbox"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
