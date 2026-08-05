import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """
    Tests that PlaidService correctly maps the 'sandbox' environment
    and sets credentials properly.
    """
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.client.api_client.configuration.api_key['clientId'] == "test_client"
    assert service.client.api_client.configuration.api_key['secret'] == "test_secret"

def test_plaid_service_initialization_production():
    """
    Tests that PlaidService correctly maps the 'production' environment.
    """
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")

    assert service.env_name == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_unknown_env():
    """
    Tests that PlaidService defaults to sandbox for unknown environments.
    """
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")

    assert service.env_name == "development"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_is_configured_true():
    """
    Tests that is_configured returns True when credentials exist.
    """
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.is_configured() is True

def test_is_configured_false_missing_secret():
    """
    Tests that is_configured returns False when secret is missing.
    """
    service = PlaidService(client_id="test_client", secret="", env="sandbox")
    assert service.is_configured() is False

def test_is_configured_false_missing_client():
    """
    Tests that is_configured returns False when client_id is missing.
    """
    service = PlaidService(client_id="", secret="test_secret", env="sandbox")
    assert service.is_configured() is False
