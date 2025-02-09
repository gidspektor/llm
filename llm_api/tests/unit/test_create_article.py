import pytest
from unittest.mock import AsyncMock, MagicMock
from llm_api.api.v1.views import create_article
from llm_api.api.v1.schemas import ArticleResponse, TextRequest


@pytest.mark.asyncio
async def test_create_article(mocker):
    """
    Test the create_article endpoint handler function.
    """
    # Mock the LlmClientFactory and CreateArticleService
    mock_llm_client = MagicMock()
    mock_llm_factory = mocker.patch("llm_api.api.v1.views.LlmClientFactory")
    mock_llm_factory().create_client.return_value = mock_llm_client

    mock_create_article_service = mocker.patch("llm_api.api.v1.views.CreateArticleService")
    mock_create_article_instance = mock_create_article_service.return_value
    mock_create_article_instance.create_article = AsyncMock(return_value={
        "title": "Generated Title",
        "body": "Generated article content"
    })

    # Prepare the request data
    request_data = TextRequest(text="This is the initial article text.")

    # Call the endpoint handler function
    response = await create_article(request=request_data)

    # Assertions
    assert isinstance(response, ArticleResponse)
    assert response.title == "Generated Title"
    assert response.body == "Generated article content"
