import openai

from llm_api.interfaces.llm_client_interface import LlmClientInterface


class OpenAIClient(LlmClientInterface):
    def __init__(self, openai_module: openai):
        self._openai = openai_module

    def set_api_key(self, api_key: str) -> None:
        """Set API key for the client."""

        self._openai.api_key = api_key
