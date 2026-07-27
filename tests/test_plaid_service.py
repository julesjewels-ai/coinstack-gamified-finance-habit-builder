import pytest
from src.services.plaid_service import PlaidService
from src.core.config import Settings
import plaid
from plaid.api import plaid_api

def test_plaid_service_initialization():
    # Setup test settings
    settings = Settings()
    settings.PLAID_CLIENT_ID = "test_client_id"
    settings.PLAID_SECRET = "test_secret"
    settings.PLAID_ENV = "sandbox"

    # Initialize service
    service = PlaidService(settings)

    # Verify the instance and methods
    assert service is not None
    assert service.env == "sandbox"
    client = service.get_client()
    assert isinstance(client, plaid_api.PlaidApi)

def test_plaid_service_production_env():
    settings = Settings()
    settings.PLAID_ENV = "production"

    service = PlaidService(settings)
    assert service.env == "production"

def test_plaid_service_development_env_fallback():
    settings = Settings()
    settings.PLAID_ENV = "development"

    service = PlaidService(settings)
    assert service.env == "development"

    # According to the rules, development environment must fall back to Sandbox Configuration
    assert service.client.api_client.configuration.host == plaid.Environment.Sandbox
