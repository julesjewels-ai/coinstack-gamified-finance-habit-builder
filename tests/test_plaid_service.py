import pytest
import os
import plaid
from src.core.config import settings
from src.services.plaid_service import PlaidService
from src.core.app import App

def test_plaid_service_initialization_sandbox(monkeypatch):
    """Test PlaidService initializes correctly with sandbox environment."""
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client_id')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')

    service = PlaidService()
    assert service.env == 'sandbox'
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_initialization_development(monkeypatch):
    """Test PlaidService initializes correctly with development environment."""
    monkeypatch.setattr(settings, 'PLAID_ENV', 'development')
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client_id')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')

    service = PlaidService()
    assert service.env == 'development'
    assert service.is_configured() is True

def test_plaid_service_initialization_production(monkeypatch):
    """Test PlaidService initializes correctly with production environment."""
    monkeypatch.setattr(settings, 'PLAID_ENV', 'production')
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client_id')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')

    service = PlaidService()
    assert service.env == 'production'
    assert service.is_configured() is True

def test_plaid_service_initialization_unknown_env(monkeypatch):
    """Test PlaidService raises error on unknown environment."""
    monkeypatch.setattr(settings, 'PLAID_ENV', 'unknown')
    with pytest.raises(ValueError, match="Unknown Plaid environment: unknown"):
        PlaidService()

def test_app_initializes_plaid_service(monkeypatch):
    """Test App correctly initializes PlaidService."""
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')
    app = App()
    assert app.plaid_service is not None
    assert isinstance(app.plaid_service, PlaidService)

def test_app_uses_injected_plaid_service(monkeypatch):
    """Test App correctly uses injected PlaidService."""
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')
    mock_service = PlaidService()
    app = App(plaid_service=mock_service)
    assert app.plaid_service is mock_service
