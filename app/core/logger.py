"""Logger setup for the smart-summary-app-backend core module.

This module configures the logging for the application using the project name from config.
"""

import logging

logger = logging.getLogger("smart-summary-backend")
logging.basicConfig(level=logging.INFO)
