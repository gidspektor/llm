from fastapi import APIRouter

from llm_api.api.v1.schemas import (
	ArticlesResponse,
	ArticleResponse,
	TextRequest,
)


from llm_api.services.llm_services.create_article_service import CreateArticleService
from llm_api.services.llm_services.rewrite_article_service import RewriteArticleService
from llm_api.factories.llm_factories.llm_client_factory import LlmClientFactory

from llm_api.services.news_services.the_news_api_service import TheNewsApiService
from llm_api.factories.news_api_factories.news_api_client_factory import NewsApiClientFactory

from llm_api.services.llm_services.make_query_service import MakeQueryService

router = APIRouter(prefix="/v1")

# Using POST because technically we are creating a new article and GET wouldn't be idempotent here
@router.post("/create", response_model=ArticleResponse)
async def create_article(request: TextRequest):
	"""
	Creates a news article from the given text.
	"""

	# Create llm client
	llm_client = LlmClientFactory().create_client()

	# Create article service and create article
	created_article = await CreateArticleService(llm_client).create_article(request.text)

	return ArticleResponse(body=created_article["body"], title=created_article["title"])

# Using POST because technically we are creating new articles and GET wouldn't be idempotent here
@router.post("/articles", response_model=ArticlesResponse)
async def get_ai_articles():
	"""
	Fetches news articles, rewrites them, and returns the rewritten articles.
	"""

	# Create news client
	news_client = NewsApiClientFactory().create_client()

	# Create news service and get articles
	articles = await TheNewsApiService(news_client).get_articles()

	# Create llm client
	llm_client = LlmClientFactory().create_client()

	# Create rewrite service and rewrite articles
	re_written_articles = await RewriteArticleService(llm_client).rewrite_articles(articles)

	return ArticlesResponse(articles=re_written_articles)

# Using POST because we are creating an article and GET wouldn't be idempotent here
@router.post("/search", response_model=ArticleResponse)
async def search_articles(request: TextRequest):
	"""
	Searches articles from the News API and returns 
	the rewritten articles based on the user query.
	"""

	# Create llm client
	llm_client = LlmClientFactory().create_client()

	# Create query for the news api
	generated_news_api_query = await MakeQueryService(llm_client).create_query(request.text)
	search_query = generated_news_api_query["search"]
	categories_query = generated_news_api_query["categories"]
	locale_query = generated_news_api_query["locale"]

	# Create news client
	news_client = NewsApiClientFactory().create_client()

	# Create news service and get articles from query
	articles = await TheNewsApiService(news_client).get_articles(search_query, categories_query, 1, locale_query)

	# Create rewrite service and rewrite articles
	created_article = await RewriteArticleService(llm_client).rewrite_articles(articles)

	return ArticleResponse(body=created_article[0]["body"], title=created_article[0]["title"])

