import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.is_configured() is True

    # Check if host was set correctly to sandbox
    assert service.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="prod_id", secret="prod_secret", env="production")

    assert service.client_id == "prod_id"
    assert service.secret == "prod_secret"
    assert service.env_name == "production"
    assert service.is_configured() is True

    # Check if host was set correctly to production
    assert service.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development_mapped_to_sandbox():
    service = PlaidService(client_id="dev_id", secret="dev_secret", env="development")

    assert service.env_name == "sandbox"
    assert service.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_empty():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
