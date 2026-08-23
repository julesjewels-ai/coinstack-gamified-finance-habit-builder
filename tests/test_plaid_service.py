import pytest
import plaid
from src.services.plaid_service import PlaidService
from plaid.api import plaid_api

def test_plaid_service_initialization_sandbox():
    """Test that the PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )

    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert isinstance(service.client, plaid_api.PlaidApi)

def test_plaid_service_environment_mapping():
    """Test that 'development' environment correctly maps to Plaid's Sandbox."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="development"
    )

    # We can inspect the internal configuration host
    host = service.client.api_client.configuration.host
    assert host == plaid.Environment.Sandbox

def test_plaid_service_production_mapping():
    """Test that 'production' environment correctly maps to Plaid's Production."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="production"
    )

    host = service.client.api_client.configuration.host
    assert host == plaid.Environment.Production

def test_plaid_service_unknown_environment_mapping():
    """Test that an unknown environment defaults safely to Sandbox."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="unknown_env"
    )

    host = service.client.api_client.configuration.host
    assert host == plaid.Environment.Sandbox
