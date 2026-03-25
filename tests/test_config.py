import os
from decouple import RepositoryEnv, Config
from src.core.config import Settings
import tempfile
import pytest

def test_settings_defaults():
    # Clear env vars that might affect this test
    if "COINSTACK_DEBUG" in os.environ:
        del os.environ["COINSTACK_DEBUG"]
    if "BANK_API_KEY" in os.environ:
        del os.environ["BANK_API_KEY"]
    if "DATABASE_URL" in os.environ:
        del os.environ["DATABASE_URL"]

    settings = Settings()
    assert settings.DEBUG_MODE is False
    assert settings.DATABASE_URL == "sqlite:///./coinstack.db"
    assert settings.PLAID_CLIENT_ID == ""
    assert settings.PLAID_SECRET == ""
    assert settings.PLAID_ENV == "sandbox"

def test_settings_with_env_vars(monkeypatch):
    monkeypatch.setenv("COINSTACK_DEBUG", "True")
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_id")
    monkeypatch.setenv("PLAID_SECRET", "test_secret")
    monkeypatch.setenv("PLAID_ENV", "production")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")

    settings = Settings()
    assert settings.DEBUG_MODE is True
    assert settings.PLAID_CLIENT_ID == "test_id"
    assert settings.PLAID_SECRET == "test_secret"
    assert settings.PLAID_ENV == "production"
    assert settings.DATABASE_URL == "sqlite:///./test.db"
