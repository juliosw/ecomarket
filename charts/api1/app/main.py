from fastapi import FastAPI, HTTPException
import asyncpg
import os


app = FastAPI()


async def get_db_connection():
    return await asyncpg.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST")
    )


@app.on_event("startup")
async def startup():
    conn = await get_db_connection()
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)
    await conn.close()


@app.post("/register")
async def register(nome: str, email: str, score: int, token: str = None):
    if token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid token")
    conn = await get_db_connection()
    await conn.execute("INSERT INTO users (nome, email, score) VALUES ($1, $2, $3)", nome, email, score)
    await conn.close()
    return {"message": "User registered successfully"}


@app.get("/users")
async def list_users(token: str = None):
    if token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=401, detail="Invalid token")
    conn = await get_db_connection()
    users = await conn.fetch("SELECT nome, email, score FROM users")
    await conn.close()
    return [{"nome": u["nome"], "email": u["email"], "score": u["score"]} for u in users]
