FROM python:3.10.14-slim-bullseye

EXPOSE 8000

# Install Poetry and dependencies
RUN apt-get update && apt-get install -y \
  && pip install poetry==1.4.2

RUN poetry config virtualenvs.create false

# Set the working directory under /app/llm_api
WORKDIR /app/llm_api

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install

# Copy the entire project to retain the `llm_api` directory
COPY . /app/llm_api

# Set environment for Python imports
ENV PYTHONPATH=/app

# Command to run the app
CMD ["poetry", "run", "python", "app/run_app.py"]
