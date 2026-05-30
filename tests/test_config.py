import pytest
from unittest import mock
from src.core.config import Settings
from src.core.app import App
from src.core.config import settings

def test_settings_default_values():
    """Test that Settings loads default values when environment variables are not set."""
    with mock.patch("src.core.config.config") as mock_config:
        # decouple.config returns its default argument if env var is missing
        mock_config.side_effect = lambda key, default=None, cast=None: default
        settings = Settings()

        assert settings.DEBUG_MODE is False
        assert settings.BANK_API_KEY == ""
        assert settings.DATABASE_URL == "sqlite:///./coinstack.db"
        assert settings.PLAID_CLIENT_ID == ""
        assert settings.PLAID_SECRET == ""
        assert settings.PLAID_ENV == "sandbox"

def test_settings_overridden_values():
    """Test that Settings correctly reads from environment variables."""
    mock_env = {
        "COINSTACK_DEBUG": True,
        "BANK_API_KEY": "test_bank_key",
        "DATABASE_URL": "postgresql://user:pass@localhost/db",
        "PLAID_CLIENT_ID": "test_plaid_id",
        "PLAID_SECRET": "test_plaid_secret",
        "PLAID_ENV": "development",
    }

    with mock.patch("src.core.config.config") as mock_config:
        mock_config.side_effect = lambda key, default=None, cast=None: cast(mock_env[key]) if cast and key in mock_env else mock_env.get(key, default)
        settings = Settings()

        assert settings.DEBUG_MODE is True
        assert settings.BANK_API_KEY == "test_bank_key"
        assert settings.DATABASE_URL == "postgresql://user:pass@localhost/db"
        assert settings.PLAID_CLIENT_ID == "test_plaid_id"
        assert settings.PLAID_SECRET == "test_plaid_secret"
        assert settings.PLAID_ENV == "development"

def test_app_debug_mode_from_settings():
    """Test that App uses DEBUG_MODE from settings if not overridden."""
    mock_settings = mock.Mock()
    mock_settings.DEBUG_MODE = True

    app = App(settings=mock_settings)
    assert app.debug_mode is True

def test_app_debug_mode_cli_override():
    """Test that CLI debug_mode overrides settings.DEBUG_MODE."""
    mock_settings = mock.Mock()
    mock_settings.DEBUG_MODE = False

    app = App(settings=mock_settings, debug_mode=True)
    assert app.debug_mode is True
