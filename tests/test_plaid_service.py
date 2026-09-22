import pytest
from unittest.mock import patch
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.is_configured() is True
    # Verify the client got created
    assert service.client is not None

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="prod_client_id", secret="prod_secret", environment="production")
    assert service.client_id == "prod_client_id"
    assert service.secret == "prod_secret"
    assert service.environment == "production"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="")
    assert service.is_configured() is False
