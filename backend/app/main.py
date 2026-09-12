from fastapi import FastAPI
from dotenv import load_dotenv
from .routes import clients
import os

load_dotenv()
print("DB URL:", os.getenv("DATABASE_URL"))
app = FastAPI(title="Stride API")
app.include_router(clients.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stride API!"}

