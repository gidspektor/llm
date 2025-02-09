from pydantic import BaseModel
from typing import List

from llm_api.app.settings import settings


class ArticleResponse(BaseModel):
	"""
	Response schema for any article.
	"""

	title: str
	body: str


class ArticlesResponse(BaseModel):
	"""
	Response schema for multiple articles.
	"""

	articles: List[ArticleResponse]


class TextRequest(BaseModel):
	"""
	Request schema for inputs.
	"""

	text: str

	class Config:
		str_max_length = settings.request_max_lenth
