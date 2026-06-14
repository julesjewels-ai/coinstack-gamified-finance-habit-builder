import pytest
from unittest.mock import patch, MagicMock
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    assert service.test_connection() is True

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.env == "production"
    assert service.test_connection() is True

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env == "development"
    assert service.test_connection() is True
    # The plaid_api environment shouldn't literally be 'development' due to deprecation mapping to Sandbox
