"""Configuration loader module for application settings.

This module defines the ConfigLoader class for managing environment-based configuration using Pydantic.
"""

from typing import ClassVar

from pydantic_settings import BaseSettings


class ConfigLoader(BaseSettings):
    """Configuration settings for the application."""

    # Binding to all interfaces is intentional for development purposes
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    env_file: ClassVar[str] = ".env"
    env_file_encoding: ClassVar[str] = "utf-8"

    project_name: str = "smart-summary-backend"
