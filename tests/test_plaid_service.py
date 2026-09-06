import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.app import App
from src.core.config import settings

def test_plaid_service_initialization():
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="sandbox")

    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.is_configured() is True

    # Check that client is initialized
    assert service.client is not None

    # Internal configuration check
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Sandbox
    assert config.api_key['clientId'] == "test_client_id"
    assert config.api_key['secret'] == "test_secret"

def test_plaid_service_environment_mapping_production():
    service = PlaidService(client_id="test", secret="test", env="production")
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Production

def test_plaid_service_environment_mapping_development():
    # 'development' is deprecated and should map to Sandbox
    service = PlaidService(client_id="test", secret="test", env="development")
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Sandbox

def test_plaid_service_unconfigured():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False

def test_app_plaid_service_injection():
    mock_service = PlaidService(client_id="mock", secret="mock", env="sandbox")
    app = App(plaid_service=mock_service)

    assert app.plaid_service is mock_service

def test_app_plaid_service_default_initialization():
    app = App()

    assert app.plaid_service is not None
    assert isinstance(app.plaid_service, PlaidService)
    assert app.plaid_service.client_id == settings.PLAID_CLIENT_ID
    assert app.plaid_service.secret == settings.PLAID_SECRET
