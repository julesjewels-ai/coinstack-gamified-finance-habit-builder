import pytest
import plaid
from src.services.plaid_service import PlaidService
from unittest.mock import patch

def test_plaid_service_initialization_sandbox():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.environment == "sandbox"
    # Internal plaid api client initialization verified by no exceptions

def test_plaid_service_initialization_development():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="development")
    assert service.environment == "development"

def test_plaid_service_initialization_production():
    service = PlaidService(client_id="test_client", secret="test_secret", environment="production")
    assert service.environment == "production"
