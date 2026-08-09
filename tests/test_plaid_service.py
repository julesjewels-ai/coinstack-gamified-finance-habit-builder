import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.client is not None
    assert service.is_configured() is True

def test_plaid_service_production_env():
    service = PlaidService(client_id="prod_client", secret="prod_secret", environment="production")

    assert service.environment == "production"
    assert service.client is not None
    assert service.is_configured() is True

def test_plaid_service_is_configured_false():
    # If client_id or secret is empty string, it should return False
    service = PlaidService(client_id="", secret="", environment="sandbox")
    assert service.is_configured() is False
