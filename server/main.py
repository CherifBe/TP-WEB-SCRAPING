from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.scraper import ScraperService
from core.config import settings
from datetime import datetime, timedelta
from typing import List
from pydantic import BaseModel, Field, validator
from enum import Enum
import os
import csv

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

class Element(str, Enum):
    PYRO = "Pyro"
    HYDRO = "Hydro"
    ANEMO = "Anemo"
    ELECTRO = "Electro"
    DENDRO = "Dendro"
    CRYO = "Cryo"
    GEO = "Geo"
    NONE = "None"

class Weapon(str, Enum):
    SWORD = "Sword"
    CLAYMORE = "Claymore"
    POLEARM = "Polearm"
    BOW = "Bow"
    CATALYST = "Catalyst"

class Character(BaseModel):
    Icon: str
    Name: str
    Quality: str
    Element: Element
    Weapon: Weapon
    Region: str
    Model_Type: str = Field(alias="Model Type")

    @validator('Icon')
    def validate_icon_url(cls, v):
        if not v.startswith('https://') and not v.endswith('.png'):
            raise ValueError("L'URL de l'icône doit être une URL HTTPS valide et se terminer par .png")
        return v

    @validator('Quality')
    def validate_quality(cls, v):
        if not v.endswith('Stars'):
            raise ValueError("La qualité doit se terminer par 'Stars'")
        try:
            stars = int(v.split()[0])
            if not 1 <= stars <= 5:
                raise ValueError()
        except:
            raise ValueError("La qualité doit être entre 1 et 5 étoiles")
        return v

    @validator('Region')
    def validate_region(cls, v):
        valid_regions = {
            "Mondstadt", "Liyue", "Inazuma", "Sumeru", 
            "Fontaine", "Natlan", "Snezhnaya", "None"
        }
        if v not in valid_regions:
            raise ValueError(f"Région invalide. Doit être une des suivantes: {', '.join(sorted(valid_regions))}")
        return v

    @validator('Model_Type')
    def validate_model_type(cls, v):
        valid_types = {
            "Tall Male", "Tall Female", 
            "Medium Male", "Medium Female", 
            "Short Female", "Short Male",
            "Aether: Medium MaleLumine: Medium Female"
        }
        if v not in valid_types:
            raise ValueError(f"Type de modèle invalide. Doit être un des suivants: {', '.join(sorted(valid_types))}")
        return v

class CharactersResponse(BaseModel):
    characters: List[Character]
    count: int
    last_updated: datetime

    @validator('count')
    def validate_count(cls, v, values):
        if 'characters' in values and v != len(values['characters']):
            raise ValueError("Le compte ne correspond pas au nombre de personnages")
        if v < 1:
            raise ValueError("La liste des personnages ne peut pas être vide")
        return v

@app.get("/genshin_characters", response_model=CharactersResponse)
async def get_genshin_characters():
    try:
        need_refresh = True
        if os.path.exists(settings.OUTPUT_FILE):
            file_time = datetime.fromtimestamp(os.path.getmtime(settings.OUTPUT_FILE))
            if datetime.now() - file_time < timedelta(hours=24):
                need_refresh = False

        if need_refresh:
            scraper_service = ScraperService()
            success, message = await scraper_service.scrape_genshin_characters_to_csv(
                settings.BASE_URL, 
                settings.OUTPUT_FILE
            )
            
            if not success:
                raise HTTPException(status_code=500, detail=message)
        
        characters_data = []
        with open(settings.OUTPUT_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                characters_data.append(row)

        if not characters_data:
            raise HTTPException(
                status_code=404, 
                detail="Aucun personnage trouvé dans les données"
            )

        return CharactersResponse(
            characters=characters_data,
            count=len(characters_data),
            last_updated=datetime.fromtimestamp(os.path.getmtime(settings.OUTPUT_FILE))
        )

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Fichier de données non trouvé"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la récupération des données: {str(e)}"
        )