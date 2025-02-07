from pydantic import BaseModel
from typing import List


class SummaryResponse(BaseModel):
    summary: str


class Article(BaseModel):
    title: str
    body: str


class ArticleResponse(BaseModel):
    articles: List[Article]
