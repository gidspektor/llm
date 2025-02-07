from fastapi import HTTPException

from llm_api.services.llm_service import LlmService
from llm_api.interfaces.llm_client_interface import LlmClientInterface


class AutoCompleteService(LlmService):
	def __init__(self, client: LlmClientInterface) -> None:
		super().__init__(client)
		self.prompt_prefix = "Complete the text:"

	async def autocomplete_text(self, prompt: str, max_tokens: int) -> str:
		try:
			prompt = f"{self.prompt_prefix} {prompt}"
			return self.create_completion(prompt, max_tokens)
		except self.client.LlmClientError as e:
			raise HTTPException(status_code=500, detail=f"LLM API error: {str(e)}")
