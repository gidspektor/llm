from abc import ABC, abstractmethod


class LlmClientInterface(ABC):
    api_key: str

    @abstractmethod
    def set_api_key(self, api_key: str) -> str:
        raise NotImplementedError("This method should be overridden by subclasses")

    class LlmClientError(Exception): ...
