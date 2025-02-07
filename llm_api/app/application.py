from pathlib import Path
import logging
import yaml

from llm_api.app.settings import settings
from llm_api.api.router import api_router

import uvicorn
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="llm_api",
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")
    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )

    return app


def set_up_logger() -> None:
	"""Set up logging configuration."""

	with open(APP_ROOT / "logging_config.yaml", "r") as file:
		config = yaml.safe_load(file)
		logging.config.dictConfig(config)


def run_app() -> None:
	"""Entrypoint of the application."""

	# Set up logging configuration
	set_up_logger()

	# Run the application with Uvicorn
	uvicorn.run(
		"llm_api.app.application:get_app",
		workers=settings.workers_count,
		host=settings.host,
		port=settings.port,
		reload=settings.reload,
	)
