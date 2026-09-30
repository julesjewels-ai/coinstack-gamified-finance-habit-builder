import pytest
import os
from unittest.mock import patch
from src.core.config import Settings
from src.core.app import App

@pytest.fixture
def mock_env():
    """Provides a mocked environment, overriding any local .env effects."""
    with patch.dict(os.environ, {
        "COINSTACK_DEBUG": "true",
        "BANK_API_KEY": "test_bank_key",
        "PLAID_CLIENT_ID": "test_plaid_client",
        "PLAID_SECRET": "test_plaid_secret",
        "PLAID_ENV": "development",
        "DATABASE_URL": "sqlite:///:memory:"
    }, clear=True):
        # We need to force python-decouple to reload from our patched os.environ.
        # Since decouple uses a global Config object that caches os.environ initially,
        # we bypass the cache by instantiating a fresh Settings object, which
        # in decouple will check os.environ.
        yield

def test_settings_loads_from_env(mock_env):
    """Test that Settings correctly parses values from the environment."""
    # Since python-decouple caches .env, we clear the cache by creating a new RepositoryEnv
    # or just relying on decouple's precedence (os.environ > .env).
    settings = Settings()
    assert settings.DEBUG_MODE is True
    assert settings.BANK_API_KEY == "test_bank_key"
    assert settings.PLAID_CLIENT_ID == "test_plaid_client"
    assert settings.PLAID_SECRET == "test_plaid_secret"
    assert settings.PLAID_ENV == "development"
    assert settings.DATABASE_URL == "sqlite:///:memory:"

def test_app_debug_mode_override():
    """Test that App overrides debug_mode when explicitly provided."""
    app = App(debug_mode=True)
    assert app.debug_mode is True

    app_false = App(debug_mode=False)
    assert app_false.debug_mode is False

def test_app_debug_mode_fallback():
    """Test that App falls back to settings when debug_mode is omitted."""
    # Temporarily modify the global settings to verify App fallback
    from src.core.config import settings
    original_debug = settings.DEBUG_MODE
    try:
        settings.DEBUG_MODE = True
        app = App(debug_mode=None)
        assert app.debug_mode is True

        settings.DEBUG_MODE = False
        app2 = App(debug_mode=None)
        assert app2.debug_mode is False
    finally:
        # Restore original state
        settings.DEBUG_MODE = original_debug
