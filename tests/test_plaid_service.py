import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox() -> None:
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")

    assert service.is_configured() is True
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    # configuration object validation
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production() -> None:
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")

    assert service.is_configured() is True
    assert service.env == "production"
    # configuration object validation
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development() -> None:
    """Test PlaidService initializes correctly with development environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")

    assert service.is_configured() is True
    assert service.env == "development"
    # configuration object validation
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_is_configured_empty() -> None:
    """Test PlaidService handles empty credentials correctly."""
    service = PlaidService(client_id="", secret="", env="sandbox")

    assert service.is_configured() is False
