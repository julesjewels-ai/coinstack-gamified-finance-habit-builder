import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.is_configured() is True
    # Verify client is created correctly
    assert service.client is not None
    # We can't easily assert the internal configuration properties, but we ensure it doesn't fail

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")
    assert service.env_name == "development"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.env_name == "production"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
