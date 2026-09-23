import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initialization with sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    assert service.is_configured() is True
    # Access private configuration from ApiClient to verify host
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService initialization with production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.env == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development():
    """Test PlaidService initialization with development environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_initialization_default():
    """Test PlaidService initialization with unknown environment falls back to sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="unknown")
    assert service.env == "unknown"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_empty():
    """Test is_configured returns False when missing credentials."""
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False

    service = PlaidService(client_id="test_id", secret="", env="sandbox")
    assert service.is_configured() is False

    service = PlaidService(client_id="", secret="test_secret", env="sandbox")
    assert service.is_configured() is False
