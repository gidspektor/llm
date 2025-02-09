## To Start the App

### With Docker
1. Run the following command:
    ```bash
    docker compose up
    ```
2. Open your browser and go to [http://localhost:3000]

### Without Docker

#### Start the Front End
1. Run the following command:
    ```bash
    npm run dev
    ```

#### Start the Backend
1. Navigate to the `llm_api` directory:
    ```bash
    cd llm_api
    ```
2. Install Poetry if you don't have it:
    ```bash
    pip install poetry
    ```
3. Install dependencies:
    ```bash
    poetry install
    ```
4. Run the app:
    ```bash
    poetry run python app/run_app.py
    ```
5. Open your browser and go to [http://localhost:3000]

To run API tests, execute the following command from the `llm_api` directory:
```bash
poetry run pytest llm_api/tests/unit/
```
