from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="Stride API")
@app.get("/")
def read_root():
    return {"message": "Welcome to the Stride API!"}
