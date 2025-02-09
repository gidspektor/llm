from fastapi import HTTPException

from llm_api.services.llm_services.llm_service import LlmService
from llm_api.interfaces.llm_interfaces.llm_client_interface import LlmClientInterface


class RewriteArticleService(LlmService):
	def __init__(self, client: LlmClientInterface) -> None:
		super().__init__(client)
		self.prompt_prefix = "Without adding any other input rewrite this \
			article so that it isn't plagarism, make it 500 words."

	async def rewrite_articles(self, articles: list) -> list:
		rewritten_articles = []

		try:
			for article in articles['data']:
				title = article['title']
				description = article['description']

				prompt = f"{self.prompt_prefix} \
					{title} {description}"

				new_article = await self.create_completion(prompt)

				article_object = self.grab_title_and_body(new_article)

				rewritten_articles.append(article_object)

			return rewritten_articles
		except Exception as e:
			raise HTTPException(status_code=500, detail=f'An error occurred on the llm service: {str(e)}') from e
