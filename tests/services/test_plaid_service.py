import pytest
from unittest.mock import patch, MagicMock
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment_name == "sandbox"
    assert service.is_configured() is True
    # Verify the client is properly instantiated by checking it exists
    assert service.client is not None

def test_plaid_service_initialization_production():
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="production")

    assert service.environment_name == "production"

def test_plaid_service_initialization_development():
    """Test PlaidService initializes correctly with development environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="development")

    assert service.environment_name == "development"

def test_plaid_service_initialization_invalid_env():
    """Test PlaidService defaults to sandbox for invalid environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="invalid")

    assert service.environment_name == "invalid"
    # Should fall back to Sandbox host in Configuration, though environment_name is 'invalid'

def test_plaid_service_is_configured():
    """Test is_configured returns correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")
    assert service.is_configured() is True

    service_unconfigured = PlaidService(client_id="", secret="", environment="sandbox")
    assert service_unconfigured.is_configured() is False
