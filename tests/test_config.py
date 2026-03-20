import os
from unittest.mock import patch
from src.core.app import App
import importlib
import src.core.config
from src.core.config import Config

def test_config_default_debug():
    """Test that debug is False by default."""
    config = Config()
    assert config.COINSTACK_DEBUG is False

@patch.dict(os.environ, {"COINSTACK_DEBUG": "True"})
def test_config_env_debug():
    """Test that debug can be set via environment variable."""
    # We must reload the module to re-evaluate the config() call at the class level
    try:
        importlib.reload(src.core.config)
        config = src.core.config.Config()
        assert config.COINSTACK_DEBUG is True
    finally:
        # Clean up by reloading without the mock
        os.environ.pop("COINSTACK_DEBUG", None)
        importlib.reload(src.core.config)

def test_app_debug_mode_from_config():
    """Test that App uses config debug mode when no argument is passed."""
    # Ensure settings.COINSTACK_DEBUG is False by default
    app = App()
    assert app.debug_mode is False

def test_app_debug_mode_override():
    """Test that App uses the passed argument, overriding config."""
    app = App(debug_mode=True)
    assert app.debug_mode is True
