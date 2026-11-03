"""
Tests for PlaidService.
"""
import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox() -> None:
    """Test PlaidService configuration for sandbox environment."""
    service = PlaidService(client_id="mock_id", secret="mock_secret", environment="sandbox")
    assert service.is_configured() is True
    assert service.client_id == "mock_id"
    assert service.secret == "mock_secret"
    assert service.environment == "sandbox"
    # Depending on plaid-python version, host could be accessible differently,
    # but we just test successful instantiation.
    assert service.client is not None

def test_plaid_service_initialization_development() -> None:
    """Test PlaidService configuration for development environment."""
    service = PlaidService(client_id="mock_id", secret="mock_secret", environment="development")
    assert service.is_configured() is True
    assert service.environment == "development"
    assert service.client is not None

def test_plaid_service_initialization_production() -> None:
    """Test PlaidService configuration for production environment."""
    service = PlaidService(client_id="mock_id", secret="mock_secret", environment="production")
    assert service.is_configured() is True
    assert service.environment == "production"
    assert service.client is not None

def test_plaid_service_initialization_unconfigured() -> None:
    """Test PlaidService configuration when credentials are empty."""
    service = PlaidService(client_id="", secret="", environment="sandbox")
    assert service.is_configured() is False
