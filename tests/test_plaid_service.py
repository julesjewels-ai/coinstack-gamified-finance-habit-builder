import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    # verify it gets mapped properly during configuration, unfortunately the plaid python
    # client doesn't expose the environment back easily but we can make sure it doesn't crash
    client = service.get_client()
    assert client is not None

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="development")
    assert service.env_name == "development"
    client = service.get_client()
    assert client is not None

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="production")
    assert service.env_name == "production"
    client = service.get_client()
    assert client is not None

def test_plaid_service_initialization_fallback():
    service = PlaidService(client_id="test_client_id", secret="test_secret", env="unknown_env")
    assert service.env_name == "unknown_env"
    client = service.get_client()
    assert client is not None
