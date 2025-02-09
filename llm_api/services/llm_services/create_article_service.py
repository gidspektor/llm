from fastapi import HTTPException

from llm_api.services.llm_services.llm_service import LlmService
from llm_api.interfaces.llm_interfaces.llm_client_interface import LlmClientInterface


class CreateArticleService(LlmService):
	def __init__(self, client: LlmClientInterface) -> None:
		super().__init__(client)
		self.prompt_prefix = "Without adding any other input make a news \
			article from this information, mention how it relates to the \
			news locale country e.g. if the locale is gb then mention \
			in the article how the article relates to england or an english business \
			and make it 500 words and make it dramatic."

	async def create_article(self, text: str) -> object:
		try:
			prompt = f"{self.prompt_prefix} {text}"

			new_article = await self.create_completion(prompt)

			article_object = self.grab_title_and_body(new_article)

			return article_object
		except Exception as e:
			raise HTTPException(status_code=500, detail=f'An error occurred on the llm service: {str(e)}') from e
