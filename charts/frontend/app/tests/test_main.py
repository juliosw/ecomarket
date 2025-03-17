from fastapi.testclient import TestClient
from main import app  # Import absoluto relativo ao diretório app/


client = TestClient(app)


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
