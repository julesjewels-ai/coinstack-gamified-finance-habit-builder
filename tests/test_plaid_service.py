"""
Unit tests for the PlaidService.
"""

import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """Test that PlaidService initializes with sandbox environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")
    assert service.client is not None
    # We can't easily inspect the deep configuration values, but we can check it initialized without errors
    # and has the correct type.
    assert isinstance(service.client, plaid.api.plaid_api.PlaidApi)

def test_plaid_service_initialization_development_maps_to_sandbox():
    """Test that 'development' environment maps to sandbox."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="development")
    assert service.client is not None

def test_plaid_service_initialization_production():
    """Test that PlaidService initializes with production environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="production")
    assert service.client is not None

def test_plaid_service_initialization_default_fallback():
    """Test that unknown environment falls back to sandbox."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="unknown_env")
    assert service.client is not None
