import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initialization with sandbox environment."""
    client_id = "test_client_id"
    secret = "test_secret"
    env = "sandbox"

    service = PlaidService(client_id, secret, env)

    assert service.client_id == client_id
    assert service.secret == secret
    assert service.env == "sandbox"
    assert service.configuration.host == plaid.Environment.Sandbox
    assert service.configuration.api_key['clientId'] == client_id
    assert service.configuration.api_key['secret'] == secret
    assert service.client is not None

def test_plaid_service_initialization_production():
    """Test PlaidService initialization with production environment."""
    client_id = "prod_client_id"
    secret = "prod_secret"
    env = "production"

    service = PlaidService(client_id, secret, env)

    assert service.client_id == client_id
    assert service.secret == secret
    assert service.env == "production"
    assert service.configuration.host == plaid.Environment.Production
    assert service.configuration.api_key['clientId'] == client_id
    assert service.configuration.api_key['secret'] == secret
    assert service.client is not None

def test_plaid_service_initialization_fallback():
    """Test PlaidService initialization falls back to sandbox for unknown environments."""
    client_id = "unknown_client_id"
    secret = "unknown_secret"
    env = "unknown_env"

    service = PlaidService(client_id, secret, env)

    assert service.client_id == client_id
    assert service.secret == secret
    assert service.env == "unknown_env"
    assert service.configuration.host == plaid.Environment.Sandbox
    assert service.configuration.api_key['clientId'] == client_id
    assert service.configuration.api_key['secret'] == secret
    assert service.client is not None

def test_plaid_service_get_client():
    """Test get_client method returns the configured PlaidApi instance."""
    service = PlaidService("id", "secret", "sandbox")
    client = service.get_client()
    assert client is not None
    assert isinstance(client, plaid.api.plaid_api.PlaidApi)
