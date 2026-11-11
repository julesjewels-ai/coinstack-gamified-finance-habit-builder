import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.config import settings

def test_plaid_service_initialization(monkeypatch):
    """Test PlaidService initializes correctly with environment settings."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')

    service = PlaidService()
    assert service.client_id == 'test_client'
    assert service.secret == 'test_secret'
    assert service.env == 'sandbox'
    assert service.is_configured() is True
    # Verify the host is Sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_production_env(monkeypatch):
    """Test PlaidService handles production environment."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'prod_client')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'prod_secret')
    monkeypatch.setattr(settings, 'PLAID_ENV', 'production')

    service = PlaidService()
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_development_env(monkeypatch):
    """Test PlaidService handles development environment correctly due to deprecation."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'dev_client')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'dev_secret')
    monkeypatch.setattr(settings, 'PLAID_ENV', 'development')

    service = PlaidService()
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_not_configured(monkeypatch):
    """Test PlaidService is_configured returns False if missing credentials."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', '')
    monkeypatch.setattr(settings, 'PLAID_SECRET', '')

    service = PlaidService()
    assert service.is_configured() is False
