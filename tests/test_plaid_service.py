import pytest
import plaid
from plaid.api import plaid_api
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )

    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert isinstance(service.client, plaid_api.PlaidApi)
    assert service.is_configured() is True
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="production"
    )

    assert service.environment == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development():
    """Test PlaidService maps deprecated development environment to sandbox."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="development"
    )

    assert service.environment == "development"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_unknown_env():
    """Test PlaidService defaults to sandbox for unknown environments."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="unknown_env"
    )

    assert service.environment == "unknown_env"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_empty():
    """Test PlaidService is_configured returns False when credentials are empty."""
    service = PlaidService(
        client_id="",
        secret="",
        environment="sandbox"
    )

    assert service.is_configured() is False
