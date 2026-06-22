import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization():
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment=plaid.Environment.Sandbox
    )

    assert service.is_configured() is True
    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"
    assert service.environment == plaid.Environment.Sandbox

def test_plaid_service_not_configured():
    service = PlaidService(
        client_id="",
        secret="",
        environment=plaid.Environment.Sandbox
    )
    assert service.is_configured() is False
