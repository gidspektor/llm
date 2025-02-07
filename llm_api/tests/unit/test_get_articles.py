import pytest
from unittest.mock import AsyncMock, MagicMock
from llm_api.api.v1.views import get_ai_articles
from llm_api.api.v1.schemas import ArticleResponse


@pytest.mark.asyncio
async def test_get_articles(mocker):
    # Mock the NewsApiService to return mock articles
    mock_news_client = mocker.patch("llm_api.api.v1.views.NewsApiService")
    mock_news_instance = mock_news_client.return_value
    mock_news_instance.get_articles = AsyncMock(return_value={'data': [
        {"title": "Original Title 2", "description": "Original article content 2"}
    ]})

    # Mock the LlmClientFactory and RewriteArticleService
    mock_llm_client = MagicMock()
    mock_llm_factory = mocker.patch("llm_api.api.v1.views.LlmClientFactory")
    mock_llm_factory().create_client.return_value = mock_llm_client

    mock_rewrite_service = mocker.patch("llm_api.api.v1.views.RewriteArticleService")
    mock_rewrite_instance = mock_rewrite_service.return_value
    mock_rewrite_instance.rewrite_articles = AsyncMock(return_value=[
        {"title": "Rewritten Title 1", "body": "Rewritten article content 1"},
        {"title": "Rewritten Title 2", "body": "Rewritten article content 2"}
    ])

    # Call the endpoint handler function
    response = await get_ai_articles()

    # Assertions
    assert isinstance(response, ArticleResponse)
    assert len(response.articles) == 2
    assert response.articles[0].title == "Rewritten Title 1"
    assert response.articles[0].body == "Rewritten article content 1"
    assert response.articles[1].title == "Rewritten Title 2"
    assert response.articles[1].body == "Rewritten article content 2"
