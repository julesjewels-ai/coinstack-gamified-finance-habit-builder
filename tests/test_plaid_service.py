import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.host == plaid.Environment.Sandbox
    assert service.client is not None

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="development")
    assert service.environment == "development"
    assert service.host == "https://development.plaid.com"
    assert service.client is not None

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="production")
    assert service.environment == "production"
    assert service.host == plaid.Environment.Production
    assert service.client is not None

def test_plaid_service_initialization_fallback():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="unknown_env")
    assert service.environment == "unknown_env"
    assert service.host == plaid.Environment.Sandbox
    assert service.client is not None
