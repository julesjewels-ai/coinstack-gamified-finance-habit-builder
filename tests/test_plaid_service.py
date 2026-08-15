import pytest
from unittest.mock import patch, MagicMock
from src.services.plaid_service import PlaidService
import plaid

def test_plaid_service_initialization_sandbox():
    """Test PlaidService initializes correctly with sandbox environment."""

    with patch('src.services.plaid_service.plaid_api.PlaidApi') as MockPlaidApi, \
         patch('src.services.plaid_service.plaid.ApiClient') as MockApiClient, \
         patch('src.services.plaid_service.plaid.Configuration') as MockConfiguration:

        service = PlaidService(
            client_id="test_client_id",
            secret="test_secret",
            environment="sandbox"
        )

        MockConfiguration.assert_called_once_with(
            host=plaid.Environment.Sandbox,
            api_key={
                'clientId': "test_client_id",
                'secret': "test_secret",
            }
        )

        MockApiClient.assert_called_once()
        MockPlaidApi.assert_called_once()
        assert service.client is not None

def test_plaid_service_initialization_production():
    """Test PlaidService initializes correctly with production environment."""

    with patch('src.services.plaid_service.plaid_api.PlaidApi') as MockPlaidApi, \
         patch('src.services.plaid_service.plaid.ApiClient') as MockApiClient, \
         patch('src.services.plaid_service.plaid.Configuration') as MockConfiguration:

        service = PlaidService(
            client_id="test_prod_id",
            secret="test_prod_secret",
            environment="production"
        )

        MockConfiguration.assert_called_once_with(
            host=plaid.Environment.Production,
            api_key={
                'clientId': "test_prod_id",
                'secret': "test_prod_secret",
            }
        )

        MockApiClient.assert_called_once()
        MockPlaidApi.assert_called_once()
        assert service.client is not None

def test_plaid_service_initialization_default_env():
    """Test PlaidService defaults to sandbox for unknown environments."""

    with patch('src.services.plaid_service.plaid_api.PlaidApi') as MockPlaidApi, \
         patch('src.services.plaid_service.plaid.ApiClient') as MockApiClient, \
         patch('src.services.plaid_service.plaid.Configuration') as MockConfiguration:

        service = PlaidService(
            client_id="test_id",
            secret="test_secret",
            environment="development" # Should map to sandbox
        )

        MockConfiguration.assert_called_once_with(
            host=plaid.Environment.Sandbox,
            api_key={
                'clientId': "test_id",
                'secret': "test_secret",
            }
        )
