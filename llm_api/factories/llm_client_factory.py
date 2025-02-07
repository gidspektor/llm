import openai

from llm_api.interfaces.llm_client_interface import LlmClientInterface
from llm_api.interfaces.llm_client_factory_interface import LlmClientFactoryInterface
from llm_api.clients.openai_client import OpenAIClient


class LlmClientFactory(LlmClientFactoryInterface):
    def create_client(self) -> LlmClientInterface:
        return OpenAIClient(openai)
