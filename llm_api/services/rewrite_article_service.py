from fastapi import HTTPException

from llm_api.services.llm_service import LlmService
from llm_api.interfaces.llm_client_interface import LlmClientInterface


class RewriteArticleService(LlmService):
	def __init__(self, client: LlmClientInterface) -> None:
		super().__init__(client)
		self.title_prompt_prefix = "make the title click baity:"
		self.body_prompt_prefix = "Without adding any other input rewrite this \
			article so that it isn't plagarism, make it 500 words:"

	async def rewrite_articles(self, articles: list) -> list:
		rewritten_articles = []
		try:
			for article in articles['data']:
				title = article['title']
				description = article['description']

				body_prompt = f"{self.body_prompt_prefix} {description}"
				title_prompt = f"{self.title_prompt_prefix} {title}"

				new_article_body = await self.create_completion(body_prompt)
				new_article_title = await self.create_completion(title_prompt)

				rewritten_articles.append({'title': new_article_title, 'body': new_article_body})

			return rewritten_articles
		except Exception as e:
			raise HTTPException(status_code=500, detail=f'An error occurred: {str(e)}') from e
