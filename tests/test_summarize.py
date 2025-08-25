"""Test cases for the /v1/summarize endpoint.

This module contains tests for the summarize endpoint, including mocking the SummaryAgent
for testing without calling the actual OpenAI API.
"""

from collections.abc import AsyncGenerator, Generator
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def mock_count_tokens() -> Generator[AsyncMock]:
    """Fixture to mock the count_tokens function."""
    with patch("app.api.summarize.count_tokens", return_value=42) as mock:
        yield mock


@pytest.fixture
def mock_generate_summary_with_agent() -> Generator[AsyncMock]:
    """Fixture to mock the generate_summary_with_agent function."""

    async def mock_generator() -> AsyncGenerator[str]:
        yield "This is a mock summary."

    with patch("app.api.summarize.generate_summary_with_agent", return_value=mock_generator()) as mock:
        yield mock


def test_summarize_endpoint(
    mock_count_tokens: AsyncMock,
    mock_generate_summary_with_agent: AsyncMock,
) -> None:
    """Test the /v1/summarize endpoint with mocked dependencies.

    Parameters
    ----------
    mock_count_tokens : AsyncMock
        The mocked count_tokens function.
    mock_generate_summary_with_agent : AsyncMock
        The mocked generate_summary_with_agent function.

    """
    client = TestClient(app)
    response = client.post("/v1/summarize", json={"text": "Test input text."})

    assert response.status_code == 200

    # Read the streamed response
    streamed_content = response.text
    assert "This is a mock summary." in streamed_content
    mock_count_tokens.assert_called_once_with("Test input text.")
    mock_generate_summary_with_agent.assert_called_once()
