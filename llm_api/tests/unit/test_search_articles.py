import pytest
from unittest.mock import AsyncMock, MagicMock
from llm_api.api.v1.views import search_articles
from llm_api.api.v1.schemas import ArticleResponse, TextRequest


@pytest.mark.asyncio
async def test_search_articles(mocker):
    """
    Test the search_articles endpoint handler function.
    """
    # Mock the LlmClientFactory
    mock_llm_client = MagicMock()
    mock_llm_factory = mocker.patch("llm_api.api.v1.views.LlmClientFactory")
    mock_llm_factory().create_client.return_value = mock_llm_client

    # Mock the MakeQueryService to simulate query creation
    mock_make_query_service = mocker.patch("llm_api.api.v1.views.MakeQueryService")
    mock_make_query_instance = mock_make_query_service.return_value
    mock_make_query_instance.create_query = AsyncMock(return_value={
        "search": "usd+gbp",  # search query
        "categories": "tech",  # categories query
        "locale": "us"         # locale query
    })

    # Mock the NewsApiClientFactory and TheNewsApiService
    mock_news_client = MagicMock()
    mock_news_factory = mocker.patch("llm_api.api.v1.views.NewsApiClientFactory")
    mock_news_factory().create_client.return_value = mock_news_client

    mock_news_service = mocker.patch("llm_api.api.v1.views.TheNewsApiService")
    mock_news_service_instance = mock_news_service.return_value
    mock_news_service_instance.get_articles = AsyncMock(return_value={
        "data": [
            {"title": "Article 1", "description": "Description of article 1", "url": "https://example.com/1"},
            {"title": "Article 2", "description": "Description of article 2", "url": "https://example.com/2"},
        ]
    })

    # Mock the RewriteArticleService to simulate rewriting articles
    mock_rewrite_service = mocker.patch("llm_api.api.v1.views.RewriteArticleService")
    mock_rewrite_service_instance = mock_rewrite_service.return_value
    mock_rewrite_service_instance.rewrite_articles = AsyncMock(return_value=[
        {"title": "Rewritten Article 1", "body": "Rewritten content of article 1"},
        {"title": "Rewritten Article 2", "body": "Rewritten content of article 2"},
    ])

    # Prepare the request data
    request_data = TextRequest(text="What are the latest articles about USD to GBP exchange rates?")

    # Call the endpoint handler function
    response = await search_articles(request=request_data)

    # Assertions
    assert isinstance(response, ArticleResponse)
    assert response.title == "Rewritten Article 1"
    assert response.body == "Rewritten content of article 1"
