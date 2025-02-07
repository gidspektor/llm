from pydantic import constr

from fastapi import APIRouter
from fastapi import Query

from llm_api.app.settings import settings

from llm_api.api.v1.schemas import (
    SummaryResponse,
	ArticleResponse,
)

from llm_api.services.rewrite_article_service import RewriteArticleService
from llm_api.factories.llm_client_factory import LlmClientFactory

from llm_api.services.news_api_service import NewsApiService

router = APIRouter()

# @router.get("/autocomplete", response_model=SummaryResponse)
# async def complete_text(
#     text: constr(max_length=settings.request_max_lenth) = Query(...),
# ):
# 	llm_client = LlmClientFactory().create_client()
# 	auto_complete_service = AutoCompleteService(llm_client)

# 	text_completion = await auto_complete_service.autocomplete_text(text)

# 	return SummaryResponse(summary=text_completion)

@router.get("/articles", response_model=ArticleResponse)
async def get_ai_articles():
	news_service = NewsApiService(settings.news_api_base_url)
	articles = await news_service.get_articles()

	llm_client = LlmClientFactory().create_client()
	rewrite_service = RewriteArticleService(llm_client)

	re_written_articles = await rewrite_service.rewrite_articles(articles)

	return ArticleResponse(articles=re_written_articles)
