import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    # Internally it maps to Sandbox and creates PlaidApi
    assert service.client is not None

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.env_name == "production"
    assert service.client is not None

def test_plaid_service_initialization_default():
    service = PlaidService(client_id="test_client", secret="test_secret")
    assert service.env_name == "sandbox"
    assert service.client is not None
