from abc import ABC, abstractmethod


class NewsApiServiceInterface(ABC):
    @abstractmethod
    async def get_articles(self) -> list:
        raise NotImplementedError("This method should be overridden by subclasses")
