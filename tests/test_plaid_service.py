import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )
    assert service.is_connected() is True
    assert service.client is not None
    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
    assert service.client.api_client.configuration.api_key['clientId'] == "test_client_id"
    assert service.client.api_client.configuration.api_key['secret'] == "test_secret"

def test_plaid_service_initialization_production():
    service = PlaidService(
        client_id="test_prod_client_id",
        secret="test_prod_secret",
        environment="production"
    )
    assert service.is_connected() is True
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_fallback():
    service = PlaidService(
        client_id="test_fallback_client_id",
        secret="test_fallback_secret",
        environment="invalid_env"
    )
    assert service.is_connected() is True
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
