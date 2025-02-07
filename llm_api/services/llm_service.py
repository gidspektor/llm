from typing import Optional

from llm_api.app.settings import settings

from llm_api.interfaces.llm_client_interface import LlmClientInterface
from llm_api.interfaces.llm_interface import LlmInterface


class LlmService(LlmInterface):
	def __init__(self, client: LlmClientInterface) -> None:
		self.client = client

	async def create_completion(self, prompt: str, max_tokens: Optional[int]) -> str:
		response = self.client.Completion.create(
			model=settings.llm_model,
			prompt=prompt,
			max_tokens=max_tokens,
			n=settings.n,
			stop=None,
			temperature=settings.temerature
		)

		return response.choices[0].text.strip()
