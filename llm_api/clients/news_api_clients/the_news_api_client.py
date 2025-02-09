import httpx

from llm_api.app.settings import settings

from llm_api.interfaces.news_api_interfaces.news_api_client_interface import NewsApiClientInterface


class TheNewsApiClient(NewsApiClientInterface):
    def __init__(self) -> None:
        self.client = httpx
        self.url = settings.news_api_base_url

    def get_client(self) -> httpx:
        """Get the httpx client instance."""

        try:
            return self.client
        except Exception as e:
            raise RuntimeError(f"The News API client error: {e}") from e

    def get_url(self) -> str:
        """Get the News API URL."""

        try:
            return self.url
        except Exception as e:
            raise RuntimeError(f"The News API URL error: {e}") from e

    def get_async_client(self) -> httpx.AsyncClient:
        """Get the httpx async client instance."""

        try:
            return self.client.AsyncClient()
        except Exception as e:
            raise RuntimeError(f"The News API async client error: {e}") from e
