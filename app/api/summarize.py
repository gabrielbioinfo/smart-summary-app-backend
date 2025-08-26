"""Summarization API endpoints.

This module defines the endpoints for text summarization.
"""

from collections.abc import AsyncGenerator
from typing import Annotated

import tiktoken
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from app.agents.summarize_agent import SummaryAgent
from app.core.config import config
from app.core.logger import logger

router = APIRouter()

print(config)

summary_agent = SummaryAgent(api_key=config.open_api_key, model_name=config.open_api_model)


class SummarizeRequest(BaseModel):
    """Request model for the summarize endpoint.

    Attributes
    ----------
    text : str
        The text to be summarized.

    """

    text: str = Field(..., min_length=1, description="Text to be summarized")


async def generate_summary_with_agent(agent: SummaryAgent, text: str) -> AsyncGenerator[str]:
    """Generate a streaming summary using the SummaryAgent."""
    try:
        summary = agent.summarize(text)
        yield summary
    except ValueError as e:
        yield f"Error: {e!s}\n"


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Count the number of tokens in the given text using tiktoken."""
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)


@router.post("/v1/summarize")
async def summarize(
    body: SummarizeRequest,
    agent: Annotated[SummaryAgent, Depends(lambda: summary_agent)],
) -> StreamingResponse:
    """Stream the summarized text back to the client."""
    if not body.text:
        return StreamingResponse((chunk for chunk in ["Error: No text provided\n"]), media_type="text/plain")

    token_count = count_tokens(body.text)
    logger.info("Number of tokens in the input text: %d", token_count)

    return StreamingResponse(generate_summary_with_agent(agent, body.text), media_type="text/event-stream")
