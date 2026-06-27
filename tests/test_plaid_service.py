import pytest
import plaid
from src.services.plaid_service import PlaidService
from unittest.mock import patch, MagicMock

def test_plaid_service_initialization_sandbox():
    """Test that the service initializes correctly with sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"

    # Access private configuration from ApiClient to verify host
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Sandbox
    assert config.api_key['clientId'] == "test_id"
    assert config.api_key['secret'] == "test_secret"

def test_plaid_service_initialization_production():
    """Test that the service initializes correctly with production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")

    assert service.env == "production"

    # Access private configuration from ApiClient to verify host
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Production

def test_plaid_service_deprecated_development_environment():
    """Test that 'development' environment correctly maps to 'sandbox' and issues a warning."""
    with patch("src.services.plaid_service.logger.warning") as mock_warning:
        service = PlaidService(client_id="test_id", secret="test_secret", env="development")

        assert service.env == "sandbox"
        mock_warning.assert_called_once()

        config = service.client.api_client.configuration
        assert config.host == plaid.Environment.Sandbox

def test_get_client():
    """Test that get_client returns the correctly initialized PlaidApi instance."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    client = service.get_client()

    assert isinstance(client, plaid.api.plaid_api.PlaidApi)
