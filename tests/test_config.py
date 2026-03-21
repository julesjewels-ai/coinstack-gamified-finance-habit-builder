"""
Unit tests for the Coinstack core config loading.
"""

import os
import importlib
import pytest
import tempfile
import builtins
from unittest import mock

@pytest.fixture
def mock_env_file():
    """Provides a temporary .env file for testing."""
    fd, path = tempfile.mkstemp(suffix=".env")
    with os.fdopen(fd, 'w') as f:
        pass
    yield path
    os.remove(path)

@mock.patch.dict(os.environ, {}, clear=True)
def test_config_default_debug():
    """
    Tests that the config loads COINSTACK_DEBUG as False by default.
    """
    import src.core.config
    importlib.reload(src.core.config)

    assert src.core.config.COINSTACK_DEBUG is False

@mock.patch.dict(os.environ, {"COINSTACK_DEBUG": "true"}, clear=True)
def test_config_custom_debug():
    """
    Tests that the config loads COINSTACK_DEBUG correctly when overridden to true.
    """
    import src.core.config
    importlib.reload(src.core.config)

    assert src.core.config.COINSTACK_DEBUG is True

@mock.patch.dict(os.environ, {"COINSTACK_DEBUG": "false"}, clear=True)
def test_config_custom_debug_false():
    """
    Tests that the config loads COINSTACK_DEBUG correctly when overridden to false.
    """
    import src.core.config
    importlib.reload(src.core.config)

    assert src.core.config.COINSTACK_DEBUG is False
