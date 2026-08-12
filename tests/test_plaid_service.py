import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    client_id = "test_client_id"
    secret = "test_secret"
    env = "sandbox"

    service = PlaidService(client_id, secret, env)

    assert service.client_id == client_id
    assert service.secret == secret
    assert service.env == env
    assert service.client is not None
    # Verify it configures with Sandbox environment
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    client_id = "test_client_id"
    secret = "test_secret"
    env = "production"

    service = PlaidService(client_id, secret, env)

    assert service.client_id == client_id
    assert service.secret == secret
    assert service.env == env
    assert service.client is not None
    # Verify it configures with Production environment
    assert service.client.api_client.configuration.host == plaid.Environment.Production
