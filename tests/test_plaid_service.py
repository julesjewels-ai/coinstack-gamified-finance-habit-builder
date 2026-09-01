import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.app import App
from unittest.mock import patch, MagicMock

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' to Plaid Sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    # configuration.host is the environment string in plaid-python
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_initialization_development_mapped_to_sandbox():
    """Test PlaidService maps 'development' to Plaid Sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' to Plaid Production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_default():
    """Test PlaidService defaults to Sandbox when env is unknown."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="unknown_env")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured():
    """Test is_configured method logic."""
    service1 = PlaidService(client_id="", secret="")
    assert service1.is_configured() is False

    service2 = PlaidService(client_id="id", secret="")
    assert service2.is_configured() is False

    service3 = PlaidService(client_id="", secret="secret")
    assert service3.is_configured() is False

    service4 = PlaidService(client_id="id", secret="secret")
    assert service4.is_configured() is True

def test_app_initializes_plaid_service():
    """Test App initializes PlaidService if not provided."""
    with patch("src.core.app.settings") as mock_settings:
        mock_settings.PLAID_CLIENT_ID = "app_test_id"
        mock_settings.PLAID_SECRET = "app_test_secret"
        mock_settings.PLAID_ENV = "sandbox"
        mock_settings.DEBUG_MODE = False

        app = App()
        assert app.plaid_service is not None
        assert app.plaid_service.client_id == "app_test_id"
        assert app.plaid_service.secret == "app_test_secret"

def test_app_uses_injected_plaid_service():
    """Test App uses the injected PlaidService if provided."""
    mock_service = MagicMock(spec=PlaidService)
    app = App(plaid_service=mock_service)

    assert app.plaid_service is mock_service
