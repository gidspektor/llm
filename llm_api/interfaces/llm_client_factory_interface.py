from abc import ABC, abstractmethod
from llm_api.interfaces.llm_client_interface import LlmClientInterface


class LlmClientFactoryInterface(ABC):
	@abstractmethod
	def create_client(self) -> LlmClientInterface:
		...
