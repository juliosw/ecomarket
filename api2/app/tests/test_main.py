import pytest
from fastapi.testclient import TestClient
from api1.app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_get_products(client):
    headers = {
        "X-Request-ID": "test-request-id",
        "X-Source-IP": "test-source-ip"
    }
    response = client.get("/products", headers=headers)
    assert response.status_code == 200
    assert "response_id" in response.json()
    assert response.json()["original_request_id"] == "test-request-id"
    