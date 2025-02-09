from abc import ABC, abstractmethod


class LlmClientInterface(ABC):
    @abstractmethod
    def get_client(self):
        raise NotImplementedError("This method should be overridden by subclasses")
