from fastapi import FastAPI, Request
import httpx
import uuid


app = FastAPI()


@app.get("/external-products")
async def get_external_products(request: Request):
    request_id = request.headers.get("X-Request-ID")
    source_ip = request.headers.get("X-Source-IP")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.publicapis.org/entries"
        )
        
        return {
            "response_id": str(uuid.uuid4()),
            "original_request_id": request_id,
            "source_ip": "api2-service",
            "destination_ip": source_ip,
            "data": response.json()
        }
        