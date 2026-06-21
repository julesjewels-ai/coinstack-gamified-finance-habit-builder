import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test that PlaidService initializes correctly with sandbox credentials."""
    client_id = "test_client_id"
    secret = "test_secret"
    environment = "sandbox"

    service = PlaidService(client_id=client_id, secret=secret, environment=environment)

    assert service.client_id == client_id
    assert service.secret == secret
    assert service.environment == environment
    assert service.is_configured() is True

    # Check that it uses the correct API client configuration
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test that PlaidService initializes correctly with production credentials."""
    service = PlaidService(client_id="test", secret="test", environment="production")
    assert service.environment == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development_fallback():
    """Test that PlaidService maps 'development' (or anything else) to Sandbox by default."""
    service = PlaidService(client_id="test", secret="test", environment="development")
    assert service.environment == "development"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_false():
    """Test is_configured when credentials are missing."""
    service1 = PlaidService(client_id="", secret="test", environment="sandbox")
    assert service1.is_configured() is False

    service2 = PlaidService(client_id="test", secret="", environment="sandbox")
    assert service2.is_configured() is False

    service3 = PlaidService(client_id="", secret="", environment="sandbox")
    assert service3.is_configured() is False
