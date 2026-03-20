from decouple import config

class Config:
    """Application configuration."""

    # Environment variables
    COINSTACK_DEBUG: bool = config('COINSTACK_DEBUG', default=False, cast=bool)

# Create a global configuration object
settings = Config()
