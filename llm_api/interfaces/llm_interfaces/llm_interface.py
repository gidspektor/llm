from abc import ABC, abstractmethod


class LlmInterface(ABC):
    @abstractmethod
    async def create_completion(self, prompt: str) -> str:
        raise NotImplementedError("This method should be overridden by subclasses")
