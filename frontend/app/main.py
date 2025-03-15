from fastapi import FastAPI, Request
import httpx
import uuid


app = FastAPI()


@app.get("/products")
async def get_products(request: Request):
    request_id = str(uuid.uuid4())
    client_ip = request.client.host

    headers = {
        "X-Request-ID": request_id,
        "X-Source-IP": client_ip,
        "X-Destination-IP": "api1-service"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://api1-service:8000/products",
            headers=headers
        )

    return response.json()
