import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes with sandbox environment by default."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")

    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.client.api_client.configuration.api_key['clientId'] == "test_id"
    assert service.client.api_client.configuration.api_key['secret'] == "test_secret"
    assert service.is_configured() is True

def test_plaid_service_initialization_production():
    """Test PlaidService initializes with production environment."""
    service = PlaidService(client_id="prod_id", secret="prod_secret", environment="production")

    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_invalid_env_defaults_to_sandbox():
    """Test PlaidService defaults to sandbox for invalid environment names."""
    service = PlaidService(client_id="dev_id", secret="dev_secret", environment="development")

    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_false_when_no_credentials():
    """Test is_configured returns False when credentials are not provided."""
    service = PlaidService(client_id="", secret="")
    assert service.is_configured() is False
