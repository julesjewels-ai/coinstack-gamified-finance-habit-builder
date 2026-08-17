import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.plaid_env == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_environment_mapping_production():
    service = PlaidService(client_id="test", secret="test", env="production")
    assert service.plaid_env == plaid.Environment.Production

def test_plaid_service_environment_mapping_fallback():
    # 'development' is deprecated in plaid-python, should map to Sandbox
    service = PlaidService(client_id="test", secret="test", env="development")
    assert service.plaid_env == plaid.Environment.Sandbox

def test_plaid_service_missing_credentials():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
