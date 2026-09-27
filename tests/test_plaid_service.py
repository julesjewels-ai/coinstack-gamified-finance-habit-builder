import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.config import settings

def test_plaid_service_initialization(monkeypatch):
    """Test PlaidService initializes correctly with mocked env vars."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client_id')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')

    service = PlaidService()

    assert service.client_id == 'test_client_id'
    assert service.secret == 'test_secret'
    assert service.env == 'sandbox'
    assert service.host == plaid.Environment.Sandbox
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_environments(monkeypatch):
    """Test PlaidService configures different environments properly."""
    # Test Development
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test')
    monkeypatch.setattr(settings, 'PLAID_ENV', 'development')
    service_dev = PlaidService()
    assert service_dev.host == "https://development.plaid.com"

    # Test Production
    monkeypatch.setattr(settings, 'PLAID_ENV', 'production')
    service_prod = PlaidService()
    assert service_prod.host == plaid.Environment.Production

def test_plaid_service_missing_config(monkeypatch):
    """Test is_configured returns False when credentials are missing."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', '')
    monkeypatch.setattr(settings, 'PLAID_SECRET', '')

    service = PlaidService()
    assert service.is_configured() is False
