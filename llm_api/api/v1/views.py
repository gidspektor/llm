from pydantic import constr

from fastapi import APIRouter
from fastapi import Query

from llm_api.app.settings import settings

from llm_api.api.v1.schemas import (
    SummaryResponse,
)

from llm_api.services.auto_complete_service import AutoCompleteService
from llm_api.factories.llm_client_factory import LlmClientFactory

router = APIRouter()

@router.get("/autocomplete", response_model=SummaryResponse)
async def complete_text(
    text: constr(max_length=settings.request_max_lenth) = Query(...),
):
	llm_client = LlmClientFactory().create_client()

	auto_complete_service = AutoCompleteService(llm_client)

	text_completion = await auto_complete_service.autocomplete_text(text)

	return SummaryResponse(summary=text_completion)
