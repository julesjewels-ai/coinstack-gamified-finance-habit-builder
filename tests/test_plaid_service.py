import pytest
from src.services.plaid_service import PlaidService
from src.core.config import Settings

def test_plaid_service_initialization_sandbox(monkeypatch):
    # Mock environment variables to override decoupled defaults safely if needed,
    # but constructing Settings instance overrides defaults based on its structure
    settings = Settings()
    settings.PLAID_CLIENT_ID = "test_client_id"
    settings.PLAID_SECRET = "test_secret"
    settings.PLAID_ENV = "sandbox"

    service = PlaidService(settings=settings)

    assert service is not None
    assert service.client is not None
    assert service.client.api_client.configuration.host == 'https://sandbox.plaid.com'
    assert 'clientId' in service.client.api_client.configuration.api_key
    assert service.client.api_client.configuration.api_key['clientId'] == 'test_client_id'

def test_plaid_service_initialization_production(monkeypatch):
    settings = Settings()
    settings.PLAID_CLIENT_ID = "test_client_id_prod"
    settings.PLAID_SECRET = "test_secret_prod"
    settings.PLAID_ENV = "production"

    service = PlaidService(settings=settings)

    assert service is not None
    assert service.client is not None
    assert service.client.api_client.configuration.host == 'https://production.plaid.com'
    assert 'clientId' in service.client.api_client.configuration.api_key
    assert service.client.api_client.configuration.api_key['clientId'] == 'test_client_id_prod'
