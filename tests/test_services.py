"""
Unit tests for external services.
"""

import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox() -> None:
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_initialization_development() -> None:
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")
    assert service.environment == "development"
    assert service.is_configured() is True
    # Verify we hit the custom host string path
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_initialization_production() -> None:
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")
    assert service.environment == "production"
    assert service.is_configured() is True
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_missing_credentials() -> None:
    with pytest.raises(ValueError, match="Plaid Client ID and Secret are required."):
        PlaidService(client_id="", secret="test_secret")

    with pytest.raises(ValueError, match="Plaid Client ID and Secret are required."):
        PlaidService(client_id="test_id", secret="")
