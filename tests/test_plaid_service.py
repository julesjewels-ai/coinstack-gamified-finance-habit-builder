import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_sandbox():
    service = PlaidService("test_client", "test_secret", "sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    # configuration is private in api_client, so we can't easily assert host directly
    # without going through internal fields, but we can check it didn't throw
    assert service.client is not None

def test_plaid_service_development():
    service = PlaidService("test_client", "test_secret", "development")
    assert service.env == "development"
    assert service.client is not None

def test_plaid_service_production():
    service = PlaidService("test_client", "test_secret", "production")
    assert service.env == "production"
    assert service.client is not None

def test_plaid_service_default_fallback():
    service = PlaidService("test_client", "test_secret", "unknown")
    assert service.env == "unknown"
    assert service.client is not None
