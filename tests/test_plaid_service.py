import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"

    # Check if configured correctly
    assert service.is_configured() is True

    # Internal client check
    assert isinstance(service.client, plaid.api.plaid_api.PlaidApi)

def test_plaid_service_initialization_production():
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.environment == "production"

def test_plaid_service_initialization_invalid_env():
    """Test PlaidService raises ValueError for invalid environment."""
    with pytest.raises(ValueError, match="Invalid Plaid environment: invalid_env"):
        PlaidService(client_id="test_id", secret="test_secret", environment="invalid_env")

def test_plaid_service_is_configured_false():
    """Test PlaidService is_configured returns False when missing credentials."""
    service = PlaidService(client_id="", secret="", environment="sandbox")
    assert service.is_configured() is False

    service2 = PlaidService(client_id="test", secret="", environment="sandbox")
    assert service2.is_configured() is False

    service3 = PlaidService(client_id="", secret="test", environment="sandbox")
    assert service3.is_configured() is False
