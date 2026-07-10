from src.core.config import settings
import pytest
from src.core.app import App
from src.core.config import settings

def test_app_debug_mode_default():
    # Store old setting
    old_debug = settings.DEBUG_MODE
    settings.DEBUG_MODE = False

    app = App(settings=settings)
    assert app.debug_mode is False

    settings.DEBUG_MODE = old_debug

def test_app_debug_mode_from_settings():
    # Store old setting
    old_debug = settings.DEBUG_MODE
    settings.DEBUG_MODE = True

    app = App(settings=settings)
    assert app.debug_mode is True

    settings.DEBUG_MODE = old_debug

def test_app_debug_mode_override():
    app = App(settings=settings, debug_mode=True)
    assert app.debug_mode is True

    app2 = App(settings=settings, debug_mode=False)
    assert app2.debug_mode is False
