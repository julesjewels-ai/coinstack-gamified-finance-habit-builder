import pytest
import os
import plaid
from src.services.plaid_service import PlaidService
from src.core.config import settings

def test_plaid_service_initialization():
    # Make sure we don't pick up host environment vars
    if "PLAID_CLIENT_ID" in os.environ:
        del os.environ["PLAID_CLIENT_ID"]
    if "PLAID_SECRET" in os.environ:
        del os.environ["PLAID_SECRET"]
    if "PLAID_ENV" in os.environ:
        del os.environ["PLAID_ENV"]

    old_client_id = settings.PLAID_CLIENT_ID
    old_secret = settings.PLAID_SECRET
    old_env = settings.PLAID_ENV

    try:
        settings.PLAID_CLIENT_ID = "test_client_id"
        settings.PLAID_SECRET = "test_secret"
        settings.PLAID_ENV = "sandbox"

        service = PlaidService()
        assert service.client_id == "test_client_id"
        assert service.secret == "test_secret"
        assert service.env_name == "sandbox"
        assert service.client is not None

        settings.PLAID_ENV = "development"
        service_dev = PlaidService()
        assert service_dev.env_name == "development"

        settings.PLAID_ENV = "production"
        service_prod = PlaidService()
        assert service_prod.env_name == "production"

    finally:
        settings.PLAID_CLIENT_ID = old_client_id
        settings.PLAID_SECRET = old_secret
        settings.PLAID_ENV = old_env
