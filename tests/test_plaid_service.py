import pytest
from src.services.plaid_service import PlaidService
from src.core.config import settings

def test_plaid_service_initialization(monkeypatch):
    monkeypatch.setattr(settings, 'PLAID_ENV', 'sandbox')
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client_id')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')

    service = PlaidService()
    assert service.client is not None

def test_plaid_service_development(monkeypatch):
    monkeypatch.setattr(settings, 'PLAID_ENV', 'development')
    monkeypatch.setattr(settings, 'PLAID_CLIENT_ID', 'test_client_id')
    monkeypatch.setattr(settings, 'PLAID_SECRET', 'test_secret')

    service = PlaidService()
    assert service.client is not None
