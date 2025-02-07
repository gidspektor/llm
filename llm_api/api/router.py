from fastapi.routing import APIRouter

from llm_api.api.v1.views import router as v1_router
from llm_api.api.v1.docs.views import router as docs_router
from llm_api.api.views import router as monitoring

api_router = APIRouter()
api_router.include_router(monitoring)
api_router.include_router(docs_router)

api_router.include_router(
    v1_router,
    tags=["data"],
)
