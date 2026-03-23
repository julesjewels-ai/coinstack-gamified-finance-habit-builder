import pytest
from unittest.mock import patch
from src.core.config import Config

def test_config_default_debug_mode():
    with patch("src.core.config.config", return_value=False) as mock_config:
        config = Config()
        assert config.DEBUG_MODE is False
        mock_config.assert_called_once_with("COINSTACK_DEBUG", default=False, cast=bool)

def test_config_debug_mode_enabled():
    with patch("src.core.config.config", return_value=True) as mock_config:
        config = Config()
        assert config.DEBUG_MODE is True
        mock_config.assert_called_once_with("COINSTACK_DEBUG", default=False, cast=bool)
