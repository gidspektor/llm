from llm_api.api.views import health_check

def test_health_check():
    """
    Test the health_check endpoint handler function.
    """
    response = health_check()
    assert response == {"status": "ok"}
