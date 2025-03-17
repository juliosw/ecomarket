from fastapi.testclient import TestClient
from api1.app.main import app


client = TestClient(app)


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
