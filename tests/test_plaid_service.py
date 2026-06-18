import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test successful initialization maps to Sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")

    assert service.is_configured() is True
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"

    # Verify the underlying plaid client is instantiated
    assert service.client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.client.api_client.configuration.api_key['clientId'] == "test_id"

def test_plaid_service_initialization_production():
    """Test environment maps to Production correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")

    assert service.is_configured() is True
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development_fallback():
    """Test 'development' and unknown environments map to Sandbox as fallback."""
    service_dev = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service_dev.client.api_client.configuration.host == plaid.Environment.Sandbox

    service_unknown = PlaidService(client_id="test_id", secret="test_secret", env="unknown_env")
    assert service_unknown.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_missing_credentials():
    """Test initialization fails gracefully when missing credentials."""
    service_no_id = PlaidService(client_id="", secret="test_secret", env="sandbox")
    assert service_no_id.is_configured() is False
    assert service_no_id.client is None

    service_no_secret = PlaidService(client_id="test_id", secret="", env="sandbox")
    assert service_no_secret.is_configured() is False
    assert service_no_secret.client is None

    service_none = PlaidService(client_id="", secret="", env="sandbox")
    assert service_none.is_configured() is False
    assert service_none.client is None
