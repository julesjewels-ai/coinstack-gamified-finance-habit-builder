import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    # configuration host should be mapped to Sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_development_mapped_to_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")
    # 'development' should map to Sandbox
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_is_configured_true():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.is_configured() is True

def test_is_configured_false_missing_secret():
    service = PlaidService(client_id="test_client", secret="", env="sandbox")
    assert service.is_configured() is False

def test_is_configured_false_missing_client_id():
    service = PlaidService(client_id="", secret="test_secret", env="sandbox")
    assert service.is_configured() is False

def test_is_configured_false_missing_both():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
