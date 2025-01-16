import csv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from services.scraper import ScraperService
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def check_server_health():
    return { 'success': 'server is okay!!' }

@app.get("/genshin_characters")
async def get_genshin_characters():
    if not os.path.exists(settings.OUTPUT_FILE):
        scraper_service = ScraperService()
        await scraper_service.scrape_genshin_characters_to_csv(settings.BASE_URL, settings.OUTPUT_FILE)
    
    characters_data = []
    with open(settings.OUTPUT_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            characters_data.append(row)

    return JSONResponse(content={"characters": characters_data})
