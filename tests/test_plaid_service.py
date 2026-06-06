import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    assert service.client is not None

def test_plaid_service_environment_mapping_sandbox():
    service = PlaidService(client_id="id", secret="secret", env="sandbox")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_environment_mapping_development():
    service = PlaidService(client_id="id", secret="secret", env="development")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_environment_mapping_production():
    service = PlaidService(client_id="id", secret="secret", env="production")
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_environment_mapping_invalid_defaults_to_sandbox():
    service = PlaidService(client_id="id", secret="secret", env="invalid_env")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
