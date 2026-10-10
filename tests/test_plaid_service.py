"""
Unit tests for the PlaidService.
"""

import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox() -> None:
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.client is not None
    assert service._get_plaid_environment() == plaid.Environment.Sandbox

def test_plaid_service_initialization_production() -> None:
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.env_name == "production"
    assert service._get_plaid_environment() == plaid.Environment.Production

def test_plaid_service_initialization_development() -> None:
    """Test PlaidService correctly resolves deprecated development environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env_name == "development"
    assert service._get_plaid_environment() == "https://development.plaid.com"

def test_plaid_service_fallback_unknown_env() -> None:
    """Test PlaidService falls back to sandbox for unknown environments."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="unknown_env")
    assert service.env_name == "unknown_env"
    assert service._get_plaid_environment() == plaid.Environment.Sandbox

def test_app_dependency_injection() -> None:
    """Test App accepts injected PlaidService."""
    from src.core.app import App

    mock_service = PlaidService(client_id="id", secret="sec", env="sandbox")
    app = App(plaid_service=mock_service)

    assert app.plaid_service is mock_service
