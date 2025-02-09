from llm_api.interfaces.news_api_interfaces.news_api_client_interface import NewsApiClientInterface
from llm_api.interfaces.news_api_interfaces.news_client_factory_interface import NewsClientFactoryInterface
from llm_api.clients.news_api_clients.the_news_api_client import TheNewsApiClient


class NewsApiClientFactory(NewsClientFactoryInterface):
    def create_client(self) -> NewsApiClientInterface:
        return TheNewsApiClient()
