import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"

    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Sandbox
    assert config.api_key['clientId'] == "test_id"
    assert config.api_key['secret'] == "test_secret"

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    config = service.client.api_client.configuration
    assert config.host == "https://development.plaid.com"

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Production

def test_plaid_service_initialization_default():
    service = PlaidService(client_id="test_id", secret="test_secret", env="unknown")
    config = service.client.api_client.configuration
    assert config.host == plaid.Environment.Sandbox
