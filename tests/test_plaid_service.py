import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    """
    Tests that PlaidService correctly initializes using the Sandbox environment.
    """
    service = PlaidService(
        client_id="test_client_id",
        secret="test_secret",
        environment="sandbox"
    )

    assert service.client_id == "test_client_id"
    assert service.secret == "test_secret"

    # Access the underlying ApiClient to check the host
    api_client = service.client.api_client
    assert api_client.configuration.host == plaid.Environment.Sandbox

    # Check that api keys are set in the configuration
    assert api_client.configuration.api_key['clientId'] == "test_client_id"
    assert api_client.configuration.api_key['secret'] == "test_secret"

def test_plaid_service_initialization_production():
    """
    Tests that PlaidService correctly initializes using the Production environment.
    """
    service = PlaidService(
        client_id="prod_client_id",
        secret="prod_secret",
        environment="production"
    )

    api_client = service.client.api_client
    assert api_client.configuration.host == plaid.Environment.Production

def test_plaid_service_initialization_development_fallback():
    """
    Tests that PlaidService falls back to Sandbox when 'development' is provided
    (since development environment is deprecated).
    """
    service = PlaidService(
        client_id="dev_client_id",
        secret="dev_secret",
        environment="development"
    )

    api_client = service.client.api_client
    assert api_client.configuration.host == plaid.Environment.Sandbox
