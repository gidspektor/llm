from typing import Optional

from llm_api.app.settings import settings

from llm_api.interfaces.llm_client_interface import LlmClientInterface
from llm_api.interfaces.llm_interface import LlmInterface


class LlmService(LlmInterface):
	def __init__(self, client: LlmClientInterface) -> None:
		self.client = client

	async def create_completion(self, prompt: str) -> str:
		response = await self.client.get_client().chat.completions.create(
			model=settings.llm_model,
			messages=[
				{"role": "user", "content": prompt}
			],
			store=True,
		)

		return response.choices[0].message.content
