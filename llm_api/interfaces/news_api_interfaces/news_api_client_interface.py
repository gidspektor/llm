import httpx
from abc import ABC, abstractmethod


class NewsApiClientInterface(ABC):
    @abstractmethod
    def get_client(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def get_url(self) -> str:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def get_async_client(self) -> httpx.AsyncClient:
        raise NotImplementedError("This method should be overridden by subclasses")
