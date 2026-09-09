import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' correctly."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )
    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.environment_name == "sandbox"
    assert service.configuration.host == plaid.Environment.Sandbox
    assert service.configuration.api_key['clientId'] == "test_client_id"
    assert service.configuration.api_key['secret'] == "test_secret"
    assert service.is_configured() is True

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' correctly."""
    service = PlaidService(
        client_id="prod_client_id",
        secret="prod_secret",
        environment="production"
    )
    assert service.environment_name == "production"
    assert service.configuration.host == plaid.Environment.Production
    assert service.is_configured() is True

def test_plaid_service_initialization_development():
    """Test PlaidService maps 'development' correctly to its host."""
    service = PlaidService(
        client_id="dev_client_id",
        secret="dev_secret",
        environment="development"
    )
    assert service.environment_name == "development"
    assert service.configuration.host == "https://development.plaid.com"
    assert service.is_configured() is True

def test_plaid_service_initialization_unknown_fallback():
    """Test PlaidService maps unknown strings to 'sandbox' fallback."""
    unknown_service = PlaidService(
        client_id="unk_client_id",
        secret="unk_secret",
        environment="unknown_env"
    )
    assert unknown_service.environment_name == "unknown_env"
    assert unknown_service.configuration.host == plaid.Environment.Sandbox
    assert unknown_service.is_configured() is True

def test_plaid_service_is_not_configured():
    """Test is_configured returns False if credentials are missing."""
    service = PlaidService(
        client_id="",
        secret="",
        environment="sandbox"
    )
    assert service.is_configured() is False