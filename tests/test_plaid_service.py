import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_defaults(monkeypatch):
    monkeypatch.setattr("src.core.config.settings.PLAID_CLIENT_ID", "default_client")
    monkeypatch.setattr("src.core.config.settings.PLAID_SECRET", "default_secret")
    monkeypatch.setattr("src.core.config.settings.PLAID_ENV", "sandbox")

    service = PlaidService()
    assert service.client_id == "default_client"
    assert service.secret == "default_secret"
    assert service.env == "sandbox"
    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_explicit():
    service = PlaidService(client_id="exp_client", secret="exp_secret", env="production")
    assert service.client_id == "exp_client"
    assert service.secret == "exp_secret"
    assert service.env == "production"
    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_development_environment():
    service = PlaidService(client_id="test", secret="test", env="development")
    assert service.env == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"
