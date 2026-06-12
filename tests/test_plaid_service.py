import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_initialization_development():
    # 'development' is deprecated and maps to 'sandbox'
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service.environment == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.environment == plaid.Environment.Production
    assert service.is_configured() is True

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="", environment="sandbox")
    assert service.is_configured() is False
