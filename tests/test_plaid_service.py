import pytest
import plaid
from plaid.api import plaid_api
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initialization with 'sandbox' environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"

    client = service.get_client()
    assert isinstance(client, plaid_api.PlaidApi)
    # the client object's inner api_client has a configuration we can inspect
    assert client.api_client.configuration.host == plaid.Environment.Sandbox


def test_plaid_service_initialization_production():
    """Test PlaidService initialization with 'production' environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="production")

    client = service.get_client()
    assert client.api_client.configuration.host == plaid.Environment.Production


def test_plaid_service_initialization_development():
    """Test PlaidService initialization with 'development' environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="development")

    client = service.get_client()
    assert client.api_client.configuration.host == "https://development.plaid.com"


def test_plaid_service_initialization_unknown_defaults_to_sandbox():
    """Test PlaidService initialization with unknown environment defaults to sandbox."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="invalid_env")

    client = service.get_client()
    assert client.api_client.configuration.host == plaid.Environment.Sandbox
