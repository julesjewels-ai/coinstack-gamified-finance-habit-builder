import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.app import App
from src.core.config import settings

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    # Ensure api is configured
    assert service.client is not None

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")
    assert service.env == "development"
    assert service.client is not None

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.env == "production"
    assert service.client is not None

def test_app_initializes_with_plaid_service(monkeypatch):
    monkeypatch.setattr(settings, "PLAID_CLIENT_ID", "app_test_client")
    monkeypatch.setattr(settings, "PLAID_SECRET", "app_test_secret")
    monkeypatch.setattr(settings, "PLAID_ENV", "sandbox")

    app = App()
    assert app.plaid_service is not None
    assert app.plaid_service.client_id == "app_test_client"
    assert app.plaid_service.secret == "app_test_secret"

def test_app_injects_plaid_service():
    mock_service = PlaidService(client_id="injected_client", secret="injected_secret", env="sandbox")
    app = App(plaid_service=mock_service)

    assert app.plaid_service is mock_service
    assert app.plaid_service.client_id == "injected_client"
