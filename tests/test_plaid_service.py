import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initialization with sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_initialization_production():
    """Test PlaidService initialization with production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")

    assert service.environment == "production"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_initialization_development_mapped_to_sandbox():
    """Test PlaidService initialization maps development to sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")

    assert service.environment == "development"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_not_configured():
    """Test PlaidService is_configured returns False when credentials are empty."""
    service = PlaidService(client_id="", secret="", environment="sandbox")

    assert service.is_configured() is False
