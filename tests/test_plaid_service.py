import pytest
import plaid
from src.services.plaid_service import PlaidService
from plaid.api import plaid_api

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes correctly with sandbox environment."""
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )

    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.environment_name == "sandbox"
    assert isinstance(service.client, plaid_api.PlaidApi)

def test_plaid_service_initialization_production():
    """Test PlaidService initializes correctly with production environment."""
    service = PlaidService(
        client_id="prod_client_id",
        secret="prod_secret",
        environment="production"
    )

    assert service.client_id == "prod_client_id"
    assert service.secret == "prod_secret"
    assert service.environment_name == "production"
    assert isinstance(service.client, plaid_api.PlaidApi)

def test_plaid_service_initialization_development():
    """Test PlaidService initializes correctly with development (mapping to sandbox)."""
    service = PlaidService(
        client_id="dev_client_id",
        secret="dev_secret",
        environment="development"
    )

    assert service.client_id == "dev_client_id"
    assert service.secret == "dev_secret"
    assert service.environment_name == "development"
    assert isinstance(service.client, plaid_api.PlaidApi)
