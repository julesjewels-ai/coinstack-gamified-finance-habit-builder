"""
Tests for the PlaidService.
"""

import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox() -> None:
    """Test initializing with sandbox environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.host == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_initialization_development() -> None:
    """Test initializing with development environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service.host == "https://development.plaid.com"
    assert service.is_configured() is True

def test_plaid_service_initialization_production() -> None:
    """Test initializing with production environment."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.host == plaid.Environment.Production
    assert service.is_configured() is True

def test_plaid_service_initialization_default() -> None:
    """Test initializing with an unknown environment defaults to sandbox."""
    service = PlaidService(client_id="test_id", secret="test_secret", environment="unknown")
    assert service.host == plaid.Environment.Sandbox
    assert service.is_configured() is True

def test_plaid_service_missing_credentials() -> None:
    """Test is_configured with missing credentials."""
    service = PlaidService(client_id="", secret="")
    assert service.is_configured() is False

def test_plaid_service_partial_credentials() -> None:
    """Test is_configured with partial credentials."""
    service = PlaidService(client_id="test_id", secret="")
    assert service.is_configured() is False
