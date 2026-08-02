import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization():
    service = PlaidService(client_id="test_id", secret="test_secret")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.client is not None

def test_plaid_service_production_environment():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.environment == "production"
    assert service.client is not None

def test_plaid_service_development_environment():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service.environment == "development"
    assert service.client is not None
