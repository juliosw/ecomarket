from fastapi import FastAPI, Request
import httpx
import uuid


app = FastAPI()


@app.get("/products")
async def get_products(request: Request):
    request_id = request.headers.get("X-Request-ID")
    source_ip = request.headers.get("X-Source-IP")
    new_request_id = str(uuid.uuid4())

    headers = {
        "X-Request-ID": new_request_id,
        "X-Source-IP": "api1-service",
        "X-Destination-IP": "api2-service"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://api2-service:8000/external-products",
            headers=headers
        )

        return {
            "response_id": str(uuid.uuid4()),
            "original_request_id": request_id,
            "source_ip": "api1-service",
            "destination_ip": source_ip,
            "data": response.json()
        }
