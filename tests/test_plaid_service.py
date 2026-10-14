"""
Unit tests for the PlaidService.
"""

import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.app import App
from src.core.config import settings

def test_plaid_service_initialization_sandbox() -> None:
    """Test PlaidService initializes with sandbox environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.host == plaid.Environment.Sandbox
    assert service.client is not None

def test_plaid_service_initialization_production() -> None:
    """Test PlaidService initializes with production environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="production")
    assert service.environment == "production"
    assert service.host == plaid.Environment.Production

def test_plaid_service_initialization_development() -> None:
    """Test PlaidService initializes with development environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="development")
    assert service.environment == "development"
    assert service.host == "https://development.plaid.com"

def test_plaid_service_initialization_invalid_fallback() -> None:
    """Test PlaidService falls back to sandbox for unknown environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="unknown_env")
    assert service.environment == "unknown_env"
    assert service.host == plaid.Environment.Sandbox

def test_app_injects_plaid_service_dependency() -> None:
    """Test App correctly uses an injected PlaidService."""
    mock_service = PlaidService(client_id="mock_id", secret="mock_secret", environment="development")
    app = App(debug_mode=True, plaid_service=mock_service)

    assert app.plaid_service is mock_service
    assert app.plaid_service.client_id == "mock_id"
    assert app.plaid_service.environment == "development"

def test_app_initializes_plaid_service_from_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test App initializes PlaidService from settings if not injected."""
    # Ensure settings has specific values
    monkeypatch.setattr(settings, "PLAID_CLIENT_ID", "env_id")
    monkeypatch.setattr(settings, "PLAID_SECRET", "env_secret")
    monkeypatch.setattr(settings, "PLAID_ENV", "sandbox")

    app = App(debug_mode=True)
    assert app.plaid_service is not None
    assert app.plaid_service.client_id == "env_id"
    assert app.plaid_service.secret == "env_secret"
    assert app.plaid_service.environment == "sandbox"
