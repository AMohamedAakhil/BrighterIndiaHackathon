from fastapi import FastAPI
import httpx

app = FastAPI()

@app.post("/")
async def fetch_url_response(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.text,
        }
