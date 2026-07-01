import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' environment correctly."""
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.configuration.host == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_initialization_development():
    """Test PlaidService maps legacy 'development' environment to 'sandbox'."""
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="development")
    assert service.env_name == "development"
    assert service.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' environment correctly."""
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="production")
    assert service.env_name == "production"
    assert service.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_unrecognized():
    """Test PlaidService defaults to Sandbox for unrecognized environments."""
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="unknown")
    assert service.env_name == "unknown"
    assert service.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_empty():
    """Test PlaidService is_configured returns False when credentials are empty."""
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
