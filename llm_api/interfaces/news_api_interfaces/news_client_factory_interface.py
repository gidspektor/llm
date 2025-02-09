from abc import ABC, abstractmethod
from llm_api.interfaces.news_api_interfaces.news_api_client_interface import NewsApiClientInterface


class NewsClientFactoryInterface(ABC):
	@abstractmethod
	def create_client(self) -> NewsApiClientInterface:
		raise NotImplementedError("This method should be overridden by subclasses")
