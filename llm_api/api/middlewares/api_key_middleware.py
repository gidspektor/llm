from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from llm_api.app.settings import settings


class APIKeyMiddleware(BaseHTTPMiddleware):
	"""
	Middleware to validate API Key in the request headers.
	"""

	async def dispatch(self, request: Request, call_next):
		# Skip API key validation for OPTIONS requests
		if request.method == "OPTIONS":
			return await call_next(request)

		# Extract the API key from headers
		api_key = request.headers.get("X-API-KEY")

		if api_key != settings.app_api_key:
			return JSONResponse(status_code=401, content={"detail": "Invalid or missing API Key"})

		# Proceed to the next request handler
		response = await call_next(request)
		return response
