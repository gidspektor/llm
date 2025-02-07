from llm_api.interfaces.llm_client_interface import LlmClientInterface
from llm_api.interfaces.llm_client_factory_interface import LlmClientFactoryInterface
from llm_api.clients.openai_async_client import OpenAIAsyncClient


class LlmClientFactory(LlmClientFactoryInterface):
    def create_client(self) -> LlmClientInterface:
        return OpenAIAsyncClient()
