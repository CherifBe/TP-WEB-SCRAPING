# Genshin Impact Character Scraper & API

This project **scrapes Genshin Impact character data** from the Fandom wiki and **exposes** it through a **FastAPI** endpoint. It retrieves character info (icon URL, name, rarity, element, weapon, region, model type) and stores everything in a local CSV file.

---

## Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Requirements](#requirements)  
4. [Installation & Usage](#installation--usage)  
5. [API Endpoints](#api-endpoints)  
6. [Customization](#customization)  
7. [License](#license)  

---

## Features

- **Scraping**:  
  - Pulls data from the [Genshin Impact Fandom Wiki](https://genshin-impact.fandom.com/wiki/Characters).  
  - Extracts character info into a CSV file (`genshin_characters.csv` by default).

- **FastAPI Backend**:  
  - Serves a JSON endpoint `/genshin_characters` to display the scraped data.  
  - Uses CORS middleware to allow requests from `http://localhost:3000` by default (modifiable).

---

## Project Structure

. ├── main.py # The main file containing scraping + FastAPI code ├── genshin_characters.csv # CSV file generated after scraping ├── requirements.txt # (Optional) Python dependencies file └── README.md # Project README (this file)

markdown
Copy

> **Note**: If you rename `main.py`, ensure you update any command references accordingly.

---

## Requirements

- **Python 3.7+**  
- **pip** (to install packages)

Recommended libraries (install them individually or via `requirements.txt`):
- `requests`
- `beautifulsoup4`
- `fastapi`
- `uvicorn`
- `python-multipart` (sometimes needed by FastAPI for form data)
- `csv` (part of the standard library, no extra installation needed)

---

## Installation & Usage

1. **Clone** or **download** this repository.

2. **Install** dependencies:  
   ```bash
   pip install requests beautifulsoup4 fastapi uvicorn
Or, if you have a requirements.txt, simply run:

bash
Copy
pip install -r requirements.txt
Run the code (assuming file is main.py):

bash
Copy
python main.py
This will:
Scrape the Genshin Impact characters from the wiki.
Generate/update genshin_characters.csv with scraped data.
Start a FastAPI server on http://127.0.0.1:8000 (if you see no server logs, it means only the scraping ran—see next step for running FastAPI explicitly).
(Alternative) Run FastAPI using Uvicorn:

bash
Copy
uvicorn main:app --reload
By default, Uvicorn listens on http://127.0.0.1:8000.
If you only want to re-run the scraping, just re-run python main.py (the script will do both by default, depending on how it’s organized).
API Endpoints
GET /genshin_characters
Returns a JSON object with the contents of the genshin_characters.csv. Example response:
json
Copy
{
  "characters": [
    {
      "Icon": "...",
      "Name": "Amber",
      "Quality": "4-Star",
      "Element": "Pyro",
      "Weapon": "Bow",
      "Region": "Mondstadt",
      "Model Type": "Medium Female"
    },
    ...
  ]
}
If genshin_characters.csv is missing, you get a 404 with an error message.
Customization
CSV File Name

Default is "genshin_characters.csv". Change the output_file variable in the script if needed.
CORS Settings

By default, only "http://localhost:3000" is allowed. Adjust in the app.add_middleware(CORSMiddleware, ...) section to fit your needs.
Scraping Logic

The code looks for a table with class "article-table sortable alternating-colors-table". If the wiki changes structure, update the selector accordingly.
If the icon["data-src"] path changes, adapt the slicing or processing in the script.
License
You can choose an open-source license (e.g. MIT) or keep it private. Include a LICENSE file if distributing.

Feel free to modify or reuse this project as needed.
Enjoy scraping Genshin data and building interesting applications with it!