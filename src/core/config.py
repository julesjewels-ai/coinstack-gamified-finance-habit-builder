"""
Configuration loading for the Coinstack application.
"""

from decouple import config

# Debug mode (true/false) - can be overridden by CLI args
COINSTACK_DEBUG = config("COINSTACK_DEBUG", default=False, cast=bool)
