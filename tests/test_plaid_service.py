import pytest
from unittest.mock import patch, MagicMock

from src.services.plaid_service import PlaidService
import plaid
from plaid.api import plaid_api

def test_plaid_service_initialization_sandbox():
    with patch("src.services.plaid_service.plaid.Configuration") as mock_config, \
         patch("src.services.plaid_service.plaid.ApiClient") as mock_api_client, \
         patch("src.services.plaid_service.plaid_api.PlaidApi") as mock_plaid_api:

        service = PlaidService(client_id="test_id", secret="test_secret", env="sandbox")

        # Verify Configuration was initialized correctly for sandbox
        mock_config.assert_called_once_with(
            host=plaid.Environment.Sandbox,
            api_key={
                'clientId': 'test_id',
                'secret': 'test_secret',
            }
        )

        # Verify API client was initialized with config
        mock_api_client.assert_called_once_with(mock_config.return_value)

        # Verify PlaidApi was initialized with api_client
        mock_plaid_api.assert_called_once_with(mock_api_client.return_value)

        # Verify get_client returns the mock
        assert service.get_client() == mock_plaid_api.return_value

def test_plaid_service_initialization_production():
    with patch("src.services.plaid_service.plaid.Configuration") as mock_config, \
         patch("src.services.plaid_service.plaid.ApiClient"), \
         patch("src.services.plaid_service.plaid_api.PlaidApi"):

        PlaidService(client_id="test_id", secret="test_secret", env="production")

        # Verify Configuration was initialized correctly for production
        mock_config.assert_called_once_with(
            host=plaid.Environment.Production,
            api_key={
                'clientId': 'test_id',
                'secret': 'test_secret',
            }
        )

def test_plaid_service_initialization_development():
    with patch("src.services.plaid_service.plaid.Configuration") as mock_config, \
         patch("src.services.plaid_service.plaid.ApiClient"), \
         patch("src.services.plaid_service.plaid_api.PlaidApi"):

        PlaidService(client_id="test_id", secret="test_secret", env="development")

        # Verify Configuration was initialized correctly for development URL
        mock_config.assert_called_once_with(
            host="https://development.plaid.com",
            api_key={
                'clientId': 'test_id',
                'secret': 'test_secret',
            }
        )

def test_plaid_service_initialization_invalid_env():
    with pytest.raises(ValueError, match="Invalid Plaid environment: invalid_env"):
        PlaidService(client_id="test_id", secret="test_secret", env="invalid_env")
