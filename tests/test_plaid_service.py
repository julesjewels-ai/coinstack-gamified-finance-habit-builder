import pytest
import plaid
from src.services.plaid_service import PlaidService
from plaid.api import plaid_api


def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes with sandbox environment properly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"

    client = service.get_client()
    assert isinstance(client, plaid_api.PlaidApi)
    assert client.api_client.configuration.host == plaid.Environment.Sandbox
    assert client.api_client.configuration.api_key['clientId'] == "test_id"
    assert client.api_client.configuration.api_key['secret'] == "test_secret"


def test_plaid_service_initialization_production():
    """Test PlaidService initializes with production environment properly."""
    service = PlaidService(client_id="prod_id", secret="prod_secret", env="production")

    assert service.client_id == "prod_id"
    assert service.secret == "prod_secret"

    client = service.get_client()
    assert isinstance(client, plaid_api.PlaidApi)
    assert client.api_client.configuration.host == plaid.Environment.Production
    assert client.api_client.configuration.api_key['clientId'] == "prod_id"
    assert client.api_client.configuration.api_key['secret'] == "prod_secret"


def test_plaid_service_initialization_development_maps_to_sandbox():
    """Test PlaidService maps unknown/development env to sandbox properly."""
    service = PlaidService(client_id="dev_id", secret="dev_secret", env="development")

    client = service.get_client()
    assert client.api_client.configuration.host == plaid.Environment.Sandbox
