import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox() -> None:
    """Test initializing PlaidService with sandbox environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")

    # Verify the host is set to sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    # Verify credentials
    assert service.client.api_client.configuration.api_key['clientId'] == "test_client"
    assert service.client.api_client.configuration.api_key['secret'] == "test_secret"

def test_plaid_service_initialization_production() -> None:
    """Test initializing PlaidService with production environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")

    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development() -> None:
    """Test initializing PlaidService with development environment."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")

    assert service.client.api_client.configuration.host == 'https://development.plaid.com'

def test_plaid_service_initialization_default() -> None:
    """Test initializing PlaidService with an unrecognized environment defaults to sandbox."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="invalid_env")

    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
