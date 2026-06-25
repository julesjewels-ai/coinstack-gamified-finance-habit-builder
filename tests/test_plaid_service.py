import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.config import settings

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' correctly."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service._get_plaid_environment() == plaid.Environment.Sandbox
    assert service.client is not None

def test_plaid_service_initialization_development():
    """Test PlaidService maps 'development' (deprecated) to 'sandbox' per rules."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service._get_plaid_environment() == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' to 'Production'."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service._get_plaid_environment() == plaid.Environment.Production

def test_plaid_service_initialization_uppercase():
    """Test PlaidService is case insensitive for environment mapping."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="SANDBOX")
    assert service._get_plaid_environment() == plaid.Environment.Sandbox
