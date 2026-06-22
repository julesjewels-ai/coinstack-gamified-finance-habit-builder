import os
from decouple import RepositoryEnv, Config
from src.core.config import Settings
import tempfile
import pytest

import plaid

def test_settings_defaults(monkeypatch):
    # Clear env vars that might affect this test
    monkeypatch.delenv("COINSTACK_DEBUG", raising=False)
    monkeypatch.delenv("BANK_API_KEY", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("PLAID_CLIENT_ID", raising=False)
    monkeypatch.delenv("PLAID_SECRET", raising=False)
    monkeypatch.delenv("PLAID_ENV", raising=False)

    settings = Settings()
    assert settings.DEBUG_MODE is False
    assert settings.DATABASE_URL == "sqlite:///./coinstack.db"
    assert settings.PLAID_CLIENT_ID == ""
    assert settings.PLAID_SECRET == ""
    assert settings.PLAID_ENV == plaid.Environment.Sandbox

def test_settings_with_env_vars(monkeypatch):
    monkeypatch.setenv("COINSTACK_DEBUG", "True")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")
    monkeypatch.setenv("PLAID_CLIENT_ID", "test_plaid_client_id")
    monkeypatch.setenv("PLAID_SECRET", "test_plaid_secret")
    monkeypatch.setenv("PLAID_ENV", "production")

    settings = Settings()
    assert settings.DEBUG_MODE is True
    assert settings.DATABASE_URL == "sqlite:///./test.db"
    assert settings.PLAID_CLIENT_ID == "test_plaid_client_id"
    assert settings.PLAID_SECRET == "test_plaid_secret"
    assert settings.PLAID_ENV == plaid.Environment.Production
