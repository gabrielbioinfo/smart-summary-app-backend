"""Summarization API endpoints.

This module defines the endpoints for text summarization.
"""

from collections.abc import AsyncGenerator

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

router = APIRouter()


async def generate_summary_with_llm(text: str) -> AsyncGenerator[str]:
    """Generate a streaming summary using an LLM (placeholder implementation)."""
    # Placeholder for LLM integration
    # Replace this with actual calls to your LLM API or library
    yield "Connecting to LLM...\n"
    yield f"Summarizing: {text}\n"
    yield "Summary complete.\n"


@router.post("/v1/summarize")
async def summarize(request: Request) -> StreamingResponse:
    """Stream the summarized text back to the client."""
    body = await request.json()
    text = body.get("text", "")

    if not text:
        return StreamingResponse((chunk for chunk in ["Error: No text provided\n"]), media_type="text/plain")

    return StreamingResponse(generate_summary_with_llm(text), media_type="text/event-stream")
