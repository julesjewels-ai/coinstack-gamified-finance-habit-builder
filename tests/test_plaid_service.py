"""
Unit tests for PlaidService.
"""
import pytest
import plaid
from src.services.plaid_service import PlaidService

def test_plaid_service_initialization_sandbox():
    service = PlaidService("test_client", "test_secret", "sandbox")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "sandbox"
    # Note: Plaid's host values are URLs represented as strings in plaid.Environment
    assert "sandbox.plaid.com" in service.client.api_client.configuration.host

def test_plaid_service_initialization_production():
    service = PlaidService("test_client", "test_secret", "production")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "production"
    assert "production.plaid.com" in service.client.api_client.configuration.host

def test_plaid_service_initialization_development_fallback():
    # Development was deprecated, should fallback to Sandbox
    service = PlaidService("test_client", "test_secret", "development")
    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env_name == "development"
    assert "sandbox.plaid.com" in service.client.api_client.configuration.host

def test_plaid_service_initialization_invalid_env():
    # Any unknown environment should fallback to Sandbox
    service = PlaidService("test_client", "test_secret", "invalid")
    assert service.env_name == "invalid"
    assert "sandbox.plaid.com" in service.client.api_client.configuration.host
