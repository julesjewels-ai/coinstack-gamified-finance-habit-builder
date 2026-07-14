import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"

    # In plaid-python, configuration.host is the resolved environment URL or Enum
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_fallback():
    """Test PlaidService defaults to Sandbox for unrecognized environments."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

    service_unknown = PlaidService(client_id="test_id", secret="test_secret", env="unknown")
    assert service_unknown.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_case_insensitivity():
    """Test PlaidService handles case insensitivity correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="ProDucTion")
    assert service.env == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production
