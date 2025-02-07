from fastapi import HTTPException

from llm_api.services.llm_service import LlmService
from llm_api.interfaces.llm_client_interface import LlmClientInterface


class AutoCompleteService(LlmService):
	def __init__(self, client: LlmClientInterface) -> None:
		super().__init__(client)
		self.prompt_prefix = "Complete the word or text without saying you're continuing it:"

	async def autocomplete_text(self, prompt: str) -> str:
		try:
			prompt = f"{self.prompt_prefix} {prompt}"
			return await self.create_completion(prompt)
		except self.client.LlmClientError as e:
			raise HTTPException(status_code=500, detail=f"LLM API error: {str(e)}")
