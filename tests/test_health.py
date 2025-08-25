"""Integration tests for the Smart Summary App Backend.

This module contains tests for the healthcheck endpoint.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.mark.asyncio
async def test_healthcheck() -> None:
    """Test the healthcheck endpoint."""
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
