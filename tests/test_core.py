import pytest
from src.core.app import App
from src.core.config import settings

def test_app_initialization() -> None:
    """
    Tests that the App class can be instantiated correctly.
    """
    app = App(settings=settings)
    assert app.version == "0.1.0"
    assert app.current_user is not None
    assert app.challenge_library is not None
    assert app.bank_integration is not None
    assert app._initialized is True

def test_app_initialization_with_debug_mode() -> None:
    """
    Tests that the App class can be instantiated with debug mode enabled.
    """
    app = App(settings=settings, debug_mode=True)
    assert app.debug_mode is True

def test_app_run_method_completes_without_error(capsys: pytest.CaptureFixture) -> None:
    """
    Tests that the run method executes without raising exceptions.
    It should print specific messages to stdout.
    """
    app = App(settings=settings)

    # Check that it runs without throwing
    app.run()

    # Check output
    captured = capsys.readouterr()
    assert "Coinstack App is running!" in captured.out
    assert "Analyzing financial profile..." in captured.out
