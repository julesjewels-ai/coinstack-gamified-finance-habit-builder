import plaid
from src.services.plaid_service import PlaidService


def test_plaid_service_initialization_sandbox() -> None:
    """Test PlaidService initializes with sandbox environment correctly."""
    service = PlaidService(client_id="test_client", secret="test_secret", env="sandbox")

    assert service.client_id == "test_client"
    assert service.secret == "test_secret"
    assert service.env == "sandbox"

    # Check that client exposes the right configuration
    client = service.get_client()
    assert client is not None

    # Internal ApiClient checking
    api_client = client.api_client
    assert api_client.configuration.host == plaid.Environment.Sandbox
    assert api_client.configuration.api_key["clientId"] == "test_client"
    assert api_client.configuration.api_key["secret"] == "test_secret"


def test_plaid_service_initialization_development() -> None:
    """Test PlaidService initializes with development environment correctly."""
    service = PlaidService(client_id="dev_client", secret="dev_secret", env="Development")

    assert service.env == "development"

    client = service.get_client()
    api_client = client.api_client
    assert api_client.configuration.host == "https://development.plaid.com"
    assert api_client.configuration.api_key["clientId"] == "dev_client"
    assert api_client.configuration.api_key["secret"] == "dev_secret"


def test_plaid_service_initialization_production() -> None:
    """Test PlaidService initializes with production environment correctly."""
    service = PlaidService(client_id="prod_client", secret="prod_secret", env="production")

    assert service.env == "production"

    client = service.get_client()
    api_client = client.api_client
    assert api_client.configuration.host == plaid.Environment.Production
    assert api_client.configuration.api_key["clientId"] == "prod_client"
    assert api_client.configuration.api_key["secret"] == "prod_secret"
