from openai import AsyncOpenAI

from llm_api.app.settings import settings

from llm_api.interfaces.llm_client_interface import LlmClientInterface


class OpenAIAsyncClient(LlmClientInterface):
    def __init__(self) -> None:
        self._openai = AsyncOpenAI(api_key=settings.llm_api_key)

    def get_client(self) -> AsyncOpenAI:
        """Get the OpenAI client instance."""

        try:
            return self._openai
        except Exception as e:
            raise self.OpenAIClientError(f"Failed to get OpenAI client: {e}")
