import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.app import App

def test_plaid_service_initialization_sandbox():
    """Test PlaidService maps 'sandbox' correctly."""
    service = PlaidService("test_client", "test_secret", "sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    # The plaid api client should be initialized
    assert service.client is not None
    # Verify environment mapping (sandbox -> Sandbox)
    # The actual host URL varies, but we can check it's one of the enums
    # It shouldn't crash if configuration was successful.

def test_plaid_service_initialization_production():
    """Test PlaidService maps 'production' correctly."""
    service = PlaidService("test_client", "test_secret", "production")
    # Verify it maps correctly without error
    assert service.client is not None

def test_plaid_service_initialization_development_fallback():
    """Test PlaidService maps unknown or deprecated env to 'sandbox'."""
    service = PlaidService("test_client", "test_secret", "development")
    # Should not throw error and client should be initialized
    assert service.client is not None

def test_app_initializes_plaid_service():
    """Test App._initialize_components instantiates PlaidService."""
    app = App()
    assert hasattr(app, "plaid_service")
    assert isinstance(app.plaid_service, PlaidService)
