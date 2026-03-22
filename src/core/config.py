"""
Application configuration module using python-decouple.
Handles loading environment variables and providing default values.
"""

from decouple import config

class Settings:
    """
    Application settings class.
    Loads variables from the environment or a .env file.
    """

    def __init__(self) -> None:
        """Initializes settings with values from the environment."""
        self.DEBUG_MODE: bool = config("COINSTACK_DEBUG", default=False, cast=bool)
        self.BANK_API_KEY: str = config("BANK_API_KEY", default="")
        self.DATABASE_URL: str = config("DATABASE_URL", default="sqlite:///./coinstack.db")

settings = Settings()
