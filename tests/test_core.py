"""
Unit tests for the Coinstack core application logic.
"""

from src.core.app import App
import pytest

def test_app_initialization() -> None:
    """
    Tests that the App class can be instantiated correctly.
    """
    app = App()
    assert app is not None
    assert app.debug_mode is False
    assert app.version == "0.1.0"

def test_app_initialization_with_debug_mode() -> None:
    """
    Tests that the App class can be instantiated with debug mode enabled.
    """
    app = App(debug_mode=True)
    assert app.debug_mode is True

def test_app_run_method_completes_without_error(capsys: pytest.CaptureFixture) -> None:
    """
    Tests that the run method executes without raising exceptions.
    It should print specific messages to stdout.
    """
    app = App()
    app.run()
    captured = capsys.readouterr()
    assert "Coinstack App (v0.1.0) initializing..." in captured.out
    assert "Coinstack App initialization complete." in captured.out
    assert "Coinstack App is running!" in captured.out
    assert "Application finished its primary task (MVP simulation)." in captured.out
    assert captured.err == ""
