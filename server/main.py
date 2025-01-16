import requests
from bs4 import BeautifulSoup
import csv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def scrape_genshin_characters_to_csv(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        table = soup.find("table", class_="article-table sortable alternating-colors-table")
        if not table:
            print("Tableau non trouvé sur la page.")
            return

        headers = [header.text.strip() for header in table.find_all("th")]
        
        rows = []
        for row in table.find_all("tr")[1:]:
            cells = row.find_all(["td"])
            if cells:
                icon = cells[0].find("img")
                if icon and "data-src" in icon.attrs:
                    icon_url = "/".join(icon["data-src"].split("/")[:8])  # Garder uniquement jusqu'à ".../Icon.png"
                else:
                    icon_url = ""
                
                name = cells[1].text.strip()
                quality = cells[2].find("img")["title"] if cells[2].find("img") else ""
                element = cells[3].text.strip()
                weapon = cells[4].text.strip()
                region = cells[5].text.strip()
                model_type = cells[6].text.strip()
                rows.append([icon_url, name, quality, element, weapon, region, model_type])

        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)

        print(f"Données des personnages Genshin enregistrées dans le fichier : {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

url = "https://genshin-impact.fandom.com/wiki/Characters"
output_file = "genshin_characters.csv"

@app.get("/genshin_characters")
async def get_genshin_characters():
    if not os.path.exists(output_file):
        await scrape_genshin_characters_to_csv(url, output_file)
    
    characters_data = []
    with open(output_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            characters_data.append(row)

    return JSONResponse(content={"characters": characters_data})

@app.get("/health")
async def check_server_health():
    return { 'success': 'server is okay!!' }
