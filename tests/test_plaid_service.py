import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    # configuration is private in api_client, but we can check the host
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_development_mapped_to_sandbox():
    """Test PlaidService maps 'development' (deprecated) to Sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_api_key_configuration():
    """Test API keys are correctly set in the configuration."""
    service = PlaidService(client_id="my_client", secret="my_secret")
    config = service.client.api_client.configuration
    assert config.api_key['clientId'] == "my_client"
    assert config.api_key['secret'] == "my_secret"
