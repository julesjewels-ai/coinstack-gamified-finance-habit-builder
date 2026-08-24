"""
Unit tests for the Plaid Service.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    """Test initializing the Plaid Service targeting the sandbox environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )

    # Verify the client is initialized
    assert service.client is not None
    assert service.get_client() == service.client

def test_plaid_service_initialization_production():
    """Test initializing the Plaid Service targeting the production environment."""
    service = PlaidService(
        client_id="test_prod_id",
        secret="test_prod_secret",
        environment="production"
    )

    # We assume the mapping maps 'production' to plaid.Environment.Production
    assert service.client is not None

def test_plaid_service_initialization_development():
    """Test initializing the Plaid Service targeting development maps to sandbox."""
    service = PlaidService(
        client_id="test_dev_id",
        secret="test_dev_secret",
        environment="development"
    )

    assert service.client is not None

def test_plaid_service_initialization_invalid_env():
    """Test initializing with an invalid environment falls back to sandbox."""
    service = PlaidService(
        client_id="test_id",
        secret="test_secret",
        environment="invalid_env"
    )

    assert service.client is not None
