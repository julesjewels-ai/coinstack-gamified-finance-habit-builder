"""
Unit tests for the PlaidService.
"""

from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox() -> None:
    """Test PlaidService configuration for sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.is_configured() is True

    # Check underlying configuration
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.client.api_client.configuration.api_key["clientId"] == "test_id"
    assert service.client.api_client.configuration.api_key["secret"] == "test_secret"

def test_plaid_service_initialization_production() -> None:
    """Test PlaidService configuration for production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")

    assert service.environment == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development() -> None:
    """Test PlaidService configuration for development environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")

    assert service.environment == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_not_configured() -> None:
    """Test PlaidService when initialized without full credentials."""
    service = PlaidService(client_id="", secret="", environment="sandbox")

    assert service.is_configured() is False
