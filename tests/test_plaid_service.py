import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    # configuration is bound to the ApiClient
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_production():
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.env == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_development():
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env == "development"
    assert service.client.api_client.configuration.host == 'https://development.plaid.com'
