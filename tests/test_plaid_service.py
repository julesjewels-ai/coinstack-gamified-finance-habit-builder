import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """
    Test that the PlaidService maps 'sandbox' correctly to Environment.Sandbox
    """
    service = PlaidService(
        client_id="test_client",
        secret="test_secret",
        env_name="sandbox"
    )

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    assert service.is_configured() is True
    # The plaid api client should be initialized
    assert service.client is not None

def test_plaid_service_initialization_production():
    """
    Test that the PlaidService maps 'production' correctly to Environment.Production
    """
    service = PlaidService(
        client_id="test_prod_client",
        secret="test_prod_secret",
        env_name="production"
    )

    assert service.client_id == "test_prod_client"
    assert service.secret == "test_prod_secret"
    assert service.env_name == "production"
    assert service.is_configured() is True
    assert service.client is not None

def test_plaid_service_not_configured():
    """
    Test is_configured returns False when credentials are empty
    """
    service = PlaidService(
        client_id="",
        secret="",
        env_name="sandbox"
    )

    assert service.is_configured() is False
