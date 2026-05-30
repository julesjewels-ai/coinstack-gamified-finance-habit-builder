"""
Unit tests for the Plaid Service.
"""

from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox() -> None:
    """
    Tests that PlaidService correctly initializes with the sandbox environment.
    """
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.plaid_env == plaid.Environment.Sandbox
    assert service.client is not None

def test_plaid_service_initialization_production() -> None:
    """
    Tests that PlaidService correctly initializes with the production environment.
    """
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.plaid_env == plaid.Environment.Production
    assert service.client is not None

def test_plaid_service_initialization_fallback() -> None:
    """
    Tests that PlaidService falls back to Sandbox for unknown environments like 'development'.
    """
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.plaid_env == plaid.Environment.Sandbox
    assert service.client is not None
