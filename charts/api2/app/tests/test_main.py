from fastapi.testclient import TestClient
from ..main import app  # Ajustado para import relativo


client = TestClient(app)


def test_get_products():
    response = client.get("/external-products")
    assert response.status_code == 200
