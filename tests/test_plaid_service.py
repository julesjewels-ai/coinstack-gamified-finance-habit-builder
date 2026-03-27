"""
Unit tests for the Plaid API service.
"""

from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox() -> None:
    """
    Tests that PlaidService can be initialized correctly for the sandbox environment.
    """
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.is_configured() is True
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_development() -> None:
    """
    Tests that PlaidService falls back to sandbox for 'development' (Plaid v1 deprecated it).
    """
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env_name == "development"
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production() -> None:
    """
    Tests that PlaidService can be initialized correctly for the production environment.
    """
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.env_name == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_not_configured() -> None:
    """
    Tests the is_configured method when credentials are missing.
    """
    service = PlaidService(client_id="", secret="")
    assert service.is_configured() is False
