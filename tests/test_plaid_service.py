import pytest
import plaid
from src.services.plaid_service import PlaidService
from src.core.config import settings

def test_plaid_service_initialization_defaults(monkeypatch):
    """Test PlaidService initializes with default settings."""
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')

    service = PlaidService()
    assert service.client_id == 'test_client'
    assert service.secret == 'test_secret'
    assert service.env == 'sandbox'
    assert service.client is not None

def test_plaid_service_initialization_overrides():
    """Test PlaidService initializes with provided arguments."""
    service = PlaidService(
        client_id='override_client',
        secret='override_secret',
        env='production'
    )
    assert service.client_id == 'override_client'
    assert service.secret == 'override_secret'
    assert service.env == 'production'
    assert service.client is not None

def test_plaid_service_environments():
    """Test PlaidService correctly configures host based on environment."""
    sandbox_service = PlaidService(env='sandbox')
    assert sandbox_service.client.api_client.configuration.host == plaid.Environment.Sandbox

    production_service = PlaidService(env='production')
    assert production_service.client.api_client.configuration.host == plaid.Environment.Production

    development_service = PlaidService(env='development')
    assert development_service.client.api_client.configuration.host == 'https://development.plaid.com'
