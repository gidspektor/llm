from fastapi import HTTPException

from llm_api.app.settings import settings

from llm_api.services.llm_services.llm_service import LlmService
from llm_api.interfaces.llm_interfaces.llm_client_interface import LlmClientInterface


class MakeQueryService(LlmService):
	def __init__(self, client: LlmClientInterface) -> None:
		super().__init__(client)
		self.search_term_rules = "use | for OR e.g. cat|dog \
			and + for AND e.g. cat&dog and - for NOT e.g. -dog"

		self.categories = "general | science | sports | business |  \
			health | entertainment | tech | politics | food | travel"

		self.response_structure = "  Based on what this text is asking for \
			e.g. if they say I want news stories about pie businesses in england then you just return \
			the string search:pie categories:business locale:gb and nothing else \
			with search then categories then locale in that order always: "

		self.prompt_prefix = f"Return a query string and nothing else in this format \
			search:usd+gbp categories:tech locale:gb using these search rules {self.search_term_rules} \
			and these category rules {self.categories} and these locale rules {settings.countries_map}."

	async def create_query(self, text: str) -> dict:
		"""
		Returns a dictionary containing search terms, \
		categories, and locale from an llm based on the text provided.
		"""

		try:
			prompt = f"{self.prompt_prefix} {text}"

			query_string = await self.create_completion(prompt)
			query_object = self.parse_query_string(query_string)

			return query_object
		except Exception as e:
			raise HTTPException(status_code=500, detail=f'An error occurred on the llm service: {str(e)}') from e

	def parse_query_string(self, query_string: str) -> dict:
		"""
		Parses the query string to extract search terms, categories, and locale.
		"""
		search_query = ""
		category_query = ""
		locale_query = ""

		if "search:" in query_string:
			search_query = query_string.split("search:", 1)[1].split(" categories:", 1)[0]

		if "categories:" in query_string:
			category_query = query_string.split("categories:", 1)[1].split(" locale:", 1)[0]

		if "locale:" in query_string:
			locale_query = query_string.split("locale:", 1)[1]

		return {
			'search': search_query.strip(),
			'categories': category_query.strip(),
			'locale': locale_query.strip()
		}
