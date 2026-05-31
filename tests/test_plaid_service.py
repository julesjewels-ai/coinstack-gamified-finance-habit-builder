"""
Tests for the PlaidService.
"""

import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test initializing the service with the sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.plaid_env == plaid.Environment.Sandbox
    assert service.get_client() is not None

def test_plaid_service_initialization_production():
    """Test initializing the service with the production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="production")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.env_name == "production"
    assert service.plaid_env == plaid.Environment.Production
    assert service.get_client() is not None

def test_plaid_service_initialization_development_fallback():
    """Test initializing the service with development environment falls back to sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="development")
    assert service.env_name == "development"
    assert service.plaid_env == plaid.Environment.Sandbox
    assert service.get_client() is not None

def test_plaid_service_initialization_unknown_fallback():
    """Test initializing the service with an unknown environment falls back to sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", env="unknown_env")
    assert service.env_name == "unknown_env"
    assert service.plaid_env == plaid.Environment.Sandbox
    assert service.get_client() is not None
