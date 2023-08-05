from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import get_sub

app = FastAPI()

# Configure CORS settings
origins = ["*"]  # Replace "*" with the specific origins you want to allow

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_sub")
async def fetch_url_response(link: str):
    response = get_sub(link)
    response.setHeader('Access-Control-Allow-Origin', '*');
    return response