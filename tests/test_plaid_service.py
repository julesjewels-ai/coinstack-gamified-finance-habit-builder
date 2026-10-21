import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"
    assert service.is_configured() is True
    # Verify the underlying configuration host
    # api_client.configuration.host
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")
    assert service.env == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.env == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_fallback():
    # Test that an unknown env falls back to Sandbox
    service = PlaidService(client_id="test_client", secret="test_secret", env="unknown_env")
    assert service.env == "unknown_env"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured_empty():
    service = PlaidService(client_id="", secret="", env="sandbox")
    assert service.is_configured() is False
