from fastapi import APIRouter

from llm_api.app.settings import settings

from llm_api.api.v1.schemas import (
    SummaryRequest, SummaryResponse,
)

from llm_api.services.auto_complete_service import AutoCompleteService
from llm_api.factories.llm_client_factory import LlmClientFactory

router = APIRouter()

@router.post("/autocomplete", response_model=SummaryResponse)
async def complete_text(request: SummaryRequest) -> SummaryRequest:
	llm_client = LlmClientFactory().create_client()
	llm_client.set_api_key(settings.llm_api_key)
	auto_complete_service = AutoCompleteService(llm_client)

	text = auto_complete_service.autocomplete_text(request.text, request.max_length)

	return SummaryRequest(text=text)
