from fastapi import FastAPI, HTTPException
import random
import os

app = FastAPI()

@app.get("/score")
async def generate_score(token: str = None):
    if token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"score": random.randint(100, 1000)}
