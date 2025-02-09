from fastapi import HTTPException
from typing import Optional

from llm_api.app.settings import settings

from llm_api.interfaces.news_api_interfaces.news_api_service_interface import NewsApiServiceInterface
from llm_api.interfaces.news_api_interfaces.news_api_client_interface import NewsApiClientInterface


class TheNewsApiService(NewsApiServiceInterface):
	def __init__(self, client: NewsApiClientInterface) -> None:
		self.url = client.get_url()
		self.client = client

	async def get_articles(
				self,
				search: Optional[str] = "",
				categories: Optional[str] = settings.default_categories,
				limit: Optional[int] = settings.news_stories_limit,
				locale: Optional[str] = settings.news_country,
			) -> str:
		try:
			params = {
				"api_token": settings.news_api_token,
				"categories": categories,
				"limit": limit,
				"locale": locale,
				"language": settings.news_language,
				"search": search,
			}

			async with self.client.get_async_client() as client:
				response = await client.get(self.url, params=params)
				return response.json()
		except Exception as e:
			raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}") from e
