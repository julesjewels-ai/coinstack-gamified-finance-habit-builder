"""
Unit tests for the PlaidService.
"""

from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization():
    """Test that the PlaidService initializes correctly with sandbox env."""
    client_id = "test_client_id"
    secret = "test_secret"
    env = "sandbox"

    service = PlaidService(client_id, secret, env)

    client = service.get_client()
    assert client is not None
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_env_mapping():
    """Test mapping of environment strings to Plaid Environments."""
    service = PlaidService("id", "secret", "development")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

    service2 = PlaidService("id", "secret", "production")
    assert service2.client.api_client.configuration.host == plaid.Environment.Production

    service3 = PlaidService("id", "secret", "unknown_env")
    assert service3.client.api_client.configuration.host == plaid.Environment.Sandbox
