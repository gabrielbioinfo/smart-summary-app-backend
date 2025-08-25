"""Summary Agent for interacting with the OpenAI LLM.

This module initializes the OpenAI LLM model and provides observability for its usage.
"""

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from app.core.logger import logger


class SummaryAgent:
    """Agent for summarizing text using OpenAI's LLM with chaining support."""

    def __init__(
        self,
        api_key: str,
        model_name: str = "gpt-4o-mini",
        system_prompt: str | None = None,
    ) -> None:
        """Initialize the agent with the OpenAI API key, model name, and optional system prompt."""
        self.llm = OpenAI(api_key=api_key, model=model_name)
        self.system_prompt = system_prompt
        logger.info("SummaryAgent initialized with OpenAI LLM.")

    def summarize(self, text: str) -> str:
        """Generate a summary for the given text."""
        logger.info("Generating summary for input text.")
        try:
            if self.system_prompt:
                prompt = PromptTemplate.from_template(self.system_prompt + "\n{input}")
                chain = prompt | self.llm
                summary = chain.invoke({"input": text})
            else:
                summary = self.llm(text)
        except Exception:
            logger.exception("Error during summarization")
            raise
        else:
            logger.info("Summary generated successfully.")
            return summary
