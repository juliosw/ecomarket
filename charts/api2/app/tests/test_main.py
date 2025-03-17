from fastapi.testclient import TestClient
from api2.app.main import app


client = TestClient(app)


def test_get_products():
    response = client.get("/external-products")
    assert response.status_code == 200
