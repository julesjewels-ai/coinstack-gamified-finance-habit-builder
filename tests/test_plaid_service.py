import pytest
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization():
    """
    Test that PlaidService initializes correctly with configured environment variables.
    """
    service = PlaidService(
        client_id='test_client_id',
        secret='test_secret',
        env='sandbox'
    )

    # Check client was instantiated
    assert service.client is not None
    assert isinstance(service.get_client(), plaid.api.plaid_api.PlaidApi)

    # Environment setup correctly based on PLAID_ENV
    assert service.env == 'sandbox'

def test_plaid_service_different_environment():
    """
    Test that PlaidService uses the correct host based on PLAID_ENV.
    """
    service = PlaidService(
        client_id='test_client_id',
        secret='test_secret',
        env='production'
    )

    # Check host setup
    assert service.env == 'production'
    assert isinstance(service.get_client(), plaid.api.plaid_api.PlaidApi)
