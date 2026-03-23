"""
Configuration module for the Coinstack application.
Handles loading environment variables and setting default configurations.
"""

from decouple import config

class Config:
    """
    Application configuration class.

    Loads configuration settings from environment variables or a .env file.
    Provides fallback defaults where appropriate.
    """

    @property
    def DEBUG_MODE(self) -> bool:
        """
        Indicates whether the application should run in debug mode.
        Loaded from COINSTACK_DEBUG environment variable.

        Returns:
            bool: True if debug mode is enabled, False otherwise.
        """
        return config("COINSTACK_DEBUG", default=False, cast=bool)
