import os
import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization(monkeypatch):
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_client")
    monkeypatch.setenv("PLAID_SECRET", "test_secret")
    monkeypatch.setenv("PLAID_ENV", "sandbox")

    # Reload settings after patching (simplest way is to pass args directly for tests)
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.is_configured() is True

    # Check that client was created
    assert service.client is not None

def test_plaid_service_environments():
    sandbox_service = PlaidService(client_id="id", secret="sec", env="sandbox")
    assert sandbox_service.client.api_client.configuration.host == plaid.Environment.Sandbox

    dev_service = PlaidService(client_id="id", secret="sec", env="development")
    assert dev_service.client.api_client.configuration.host == "https://development.plaid.com"

    prod_service = PlaidService(client_id="id", secret="sec", env="production")
    assert prod_service.client.api_client.configuration.host == plaid.Environment.Production

    fallback_service = PlaidService(client_id="id", secret="sec", env="unknown")
    assert fallback_service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_false():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
