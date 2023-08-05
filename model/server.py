from fastapi import FastAPI
from main import get_sub

app = FastAPI()

@app.get("/get_sub")
async def fetch_url_response(link: str):
    response = get_sub(link)
    return response
