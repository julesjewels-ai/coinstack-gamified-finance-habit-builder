import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.env_name == "sandbox"
    assert service.configuration.host == plaid.Environment.Sandbox
    assert service.configuration.api_key['clientId'] == "test_client"
    assert service.configuration.api_key['secret'] == "test_secret"
    assert service.client is not None

def test_plaid_service_production():
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.env_name == "production"
    assert service.configuration.host == plaid.Environment.Production

def test_plaid_service_development():
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")
    assert service.env_name == "development"
    assert service.configuration.host == 'https://development.plaid.com'

def test_plaid_service_unknown_defaults_to_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="unknown_env")
    assert service.env_name == "unknown_env"
    assert service.configuration.host == plaid.Environment.Sandbox
