"""
Tests for the Plaid Service.
"""

import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes with sandbox environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"

    # Verify the underlying ApiClient configuration
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_production():
    """Test PlaidService initializes with production environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "production"

    # Verify the underlying ApiClient configuration
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_default_sandbox():
    """Test PlaidService falls back to sandbox for unknown environments like development."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "development"

    # Verify the underlying ApiClient configuration
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_is_configured():
    """Test the is_configured method."""
    service1 = PlaidService(client_id="id", secret="secret", env="sandbox")
    assert service1.is_configured() is True

    service2 = PlaidService(client_id="", secret="secret", env="sandbox")
    assert service2.is_configured() is False

    service3 = PlaidService(client_id="id", secret="", env="sandbox")
    assert service3.is_configured() is False
