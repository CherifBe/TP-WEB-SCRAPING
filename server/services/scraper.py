import requests
from bs4 import BeautifulSoup
import csv

class ScraperService:
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