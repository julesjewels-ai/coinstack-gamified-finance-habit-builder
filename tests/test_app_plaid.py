import pytest
from src.core.app import App
from src.core.config import settings
from unittest.mock import patch

def test_app_initializes_plaid_service(monkeypatch):
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_client_id")
    monkeypatch.setenv("PLAID_SECRET", "test_secret")

    # Reload settings to pick up new env vars
    # A bit hacky, but python-decouple caches some stuff, wait we can just patch settings

    with patch.object(settings, 'PLAID_CLIENT_ID', 'test_client_id'), \
         patch.object(settings, 'PLAID_SECRET', 'test_secret'), \
         patch.object(settings, 'PLAID_ENV', 'sandbox'):
        app = App()
        assert app.plaid_service is not None
        assert app.plaid_service.client_id == 'test_client_id'
        assert app.plaid_service.environment == 'sandbox'

def test_app_skips_plaid_if_no_credentials():
    with patch.object(settings, 'PLAID_CLIENT_ID', ''), \
         patch.object(settings, 'PLAID_SECRET', ''):
        app = App()
        assert app.plaid_service is None
