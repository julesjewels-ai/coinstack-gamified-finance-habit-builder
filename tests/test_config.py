import os
from decouple import RepositoryEnv, Config
from src.core.config import Settings
import tempfile
import pytest

def test_settings_defaults():
    # Clear env vars that might affect this test
    if "COINSTACK_DEBUG" in os.environ:
        del os.environ["COINSTACK_DEBUG"]
    if "PLAID_CLIENT_ID" in os.environ:
        del os.environ["PLAID_CLIENT_ID"]
    if "PLAID_SECRET" in os.environ:
        del os.environ["PLAID_SECRET"]
    if "PLAID_ENV" in os.environ:
        del os.environ["PLAID_ENV"]
    if "DATABASE_URL" in os.environ:
        del os.environ["DATABASE_URL"]

    settings = Settings()
    assert settings.DEBUG_MODE is False
    assert settings.PLAID_CLIENT_ID == ""
    assert settings.PLAID_SECRET == ""
    assert settings.PLAID_ENV == "sandbox"
    assert settings.DATABASE_URL == "sqlite:///./coinstack.db"

def test_settings_with_env_vars(monkeypatch):
    monkeypatch.setenv("COINSTACK_DEBUG", "True")
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_client_id")
    monkeypatch.setenv("PLAID_SECRET", "test_secret")
    monkeypatch.setenv("PLAID_ENV", "production")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")

    settings = Settings()
    assert settings.DEBUG_MODE is True
    assert settings.PLAID_CLIENT_ID == "test_client_id"
    assert settings.PLAID_SECRET == "test_secret"
    assert settings.PLAID_ENV == "production"
    assert settings.DATABASE_URL == "sqlite:///./test.db"
