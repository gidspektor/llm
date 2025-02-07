import httpx

from llm_api.app.settings import settings

from llm_api.interfaces.news_api_service_interface import NewsApiServiceInterface


class NewsApiService(NewsApiServiceInterface):
	def __init__(self, url: str) -> None:
		self.url = url

	async def get_articles(self) -> str:
		try:
			params = {
				'api_token': settings.news_api_token,
				'categories': 'tech',
				'limit': settings.news_stories_limit,
				'locale': settings.news_country,
				'language': settings.news_language,
			}

			async with httpx.AsyncClient() as client:
				response = await client.get(self.url, params=params)
				response.raise_for_status()
				return response.json()
		except httpx.HTTPStatusError as e:
			raise Exception(f"News API error: {e.response.status_code})")
