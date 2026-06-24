import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_sandbox():
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )
    assert service is not None
    client = service.get_client()
    assert client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_development():
    """Test PlaidService initializes correctly with development mapping to sandbox."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="development"
    )
    assert service is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_production():
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="production"
    )
    assert service is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_invalid_env():
    """Test PlaidService raises ValueError with invalid environment."""
    with pytest.raises(ValueError, match="Unsupported Plaid environment: invalid_env"):
        PlaidService(
            client_id="test_client_id",
            secret="test_secret",
            environment="invalid_env"
        )
