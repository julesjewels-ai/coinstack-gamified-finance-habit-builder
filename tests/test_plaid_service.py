import pytest
from unittest.mock import patch, MagicMock
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="sandbox")

    assert service.client_id == "test_id"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    assert service.is_configured() is True

    # Check internal client setup
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="development")

    assert service.environment == "development"
    assert service.client.api_client.configuration.host == "https://development.plaid.com"

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_id", secret="test_secret", environment="production")

    assert service.environment == "production"
    assert service.client.api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_not_configured():
    service = PlaidService(client_id="", secret="", environment="sandbox")

    assert service.is_configured() is False
