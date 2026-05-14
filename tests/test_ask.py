from fastapi.testclient import TestClient
from unittest.mock import patch

from src.app.main import app


client = TestClient(app)


@patch("src.app.api.routes.pipeline.ask")
def test_ask_endpoint(mock_ask):

    mock_ask.return_value = {
        "answer": "Mocked response"
    }

    payload = {
        "query": "What is RAG?"
    }

    response = client.post("/ask", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["answer"] == "Mocked response"