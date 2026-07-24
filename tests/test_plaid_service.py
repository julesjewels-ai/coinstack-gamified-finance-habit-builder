import pytest
from src.services.plaid_service import PlaidService
from src.core.config import Settings
import plaid

def test_plaid_service_initialization(monkeypatch):
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_id")
    monkeypatch.setenv("PLAID_SECRET", "test_secret")
    monkeypatch.setenv("PLAID_ENV", "sandbox")

    settings = Settings()
    service = PlaidService(settings)

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_production_env(monkeypatch):
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_id")
    monkeypatch.setenv("PLAID_SECRET", "test_secret")
    monkeypatch.setenv("PLAID_ENV", "production")

    settings = Settings()
    service = PlaidService(settings)

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.is_configured() is True
    # In plaid-python, configuration.host holds the environment URL.
    # Production is 'https://production.plaid.com'
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_missing_credentials(monkeypatch):
    monkeypatch.setenv("PLAID_CLIENT_ID", "")
    monkeypatch.setenv("PLAID_SECRET", "")
    monkeypatch.setenv("PLAID_ENV", "sandbox")

    settings = Settings()
    service = PlaidService(settings)

    assert service.is_configured() is False
