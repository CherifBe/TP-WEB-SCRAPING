Genshin Character Scraper & API
This project provides a FastAPI backend that:

Scrapes Genshin Impact character data from the Genshin Impact Fandom Wiki.
Stores the scraped data in a CSV file.
Serves the data as a JSON API endpoint.
Table of Contents
Project Overview
Project Structure
Requirements
Installation
Usage
1. Run the Scraping Script
2. Run the FastAPI Server
3. Access the Data
Customization
Contributing
License
Project Overview
This project:

Scrapes https://genshin-impact.fandom.com/wiki/Characters to obtain a table of characters, including:

Icon URL
Name
Quality (e.g., 4* or 5*)
Element
Weapon
Region
Model Type
Saves the scraped data to genshin_characters.csv.

Exposes an API endpoint (/genshin_characters) that returns the CSV data as JSON.

Tech stack:

requests + BeautifulSoup for HTML scraping
CSV for data storage
FastAPI for the API
CORS middleware enabled to allow calls from, for example, http://localhost:3000.
Project Structure
graphql
Copy
.
├── main.py                  # The primary FastAPI + scraping script
├── genshin_characters.csv   # Auto-generated CSV after scraping (ignored initially if not existing)
├── requirements.txt         # (Optional) Might contain the Python dependencies
├── README.md                # Project documentation (this file)
└── ... (other project files as needed)
Requirements
Python 3.7+ (tested on newer versions as well)
pip (comes with most Python installations)
Below are the main dependencies:

requests (HTTP requests)
beautifulsoup4 (HTML parsing)
fastapi (the API framework)
uvicorn (ASGI server to run FastAPI)
csv (Python standard library, no extra install needed)
If you want to use a virtual environment, you can create and activate it:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Then install dependencies (if you have a requirements.txt):

bash
Copy
pip install -r requirements.txt
Or install them individually:

bash
Copy
pip install requests beautifulsoup4 fastapi uvicorn
Installation
Clone or download the repository.

Install dependencies (see above). For example:

bash
Copy
pip install requests beautifulsoup4 fastapi uvicorn
(Optional) Create a .env or environment variables if you need a custom configuration. By default, no extra environment variables are needed.

Usage
1. Run the Scraping Script
To scrape the Genshin characters page and save the data in genshin_characters.csv, you can just run the script (assuming it’s named main.py):

bash
Copy
python main.py
During execution:

The script sends a GET request to Genshin Characters Wiki.
It locates the main table with CSS classes "article-table sortable alternating-colors-table".
Extracts each row’s columns, including the icon image URL, character name, quality (stars), element, weapon, region, and model type.
Writes this data to a CSV file named genshin_characters.csv.
2. Run the FastAPI Server
After scraping is done, the FastAPI application is also defined in main.py. You can run it using uvicorn:

bash
Copy
uvicorn main:app --reload
Note: If your file is named differently, adjust the command. The pattern is uvicorn <python-file>:<FastAPI-object> --reload.

By default, uvicorn serves on http://127.0.0.1:8000.
3. Access the Data
The API endpoint to get the characters in JSON format is:

bash
Copy
GET /genshin_characters
So, open http://127.0.0.1:8000/genshin_characters in your browser or make a request via curl or Postman. If the CSV file exists, you’ll see a JSON response like:

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
If the CSV file isn’t found (meaning the scrape didn’t run or failed), you’ll get a 404 JSON response with an error message.

Customization
Output CSV: Change the filename by editing the output_file variable in the script:

python
Copy
output_file = "some_other_file.csv"
CORS Configuration:
In main.py, we’ve set allow_origins=["http://localhost:3000"]. If you want to call this API from a different domain or multiple domains, update the list as needed:

python
Copy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://my-other-site.com", "http://another-host:8080"],
    ...
)
Scraping Logic:

If the wiki changes its HTML structure, you might need to update the selectors:
python
Copy
table = soup.find("table", class_="article-table sortable alternating-colors-table")
Adjust how you parse columns or how many columns you extract.
Error Handling:

If any field is missing in a row, the script prints a message or sets a default string.
You could add more robust error handling or logging as needed.
Contributing
Fork the repository.
Create a feature branch.
Commit your changes.
Open a Pull Request.
We welcome improvements for parsing, error handling, or additional endpoints.

License
This project is released under the MIT License (or whichever license you choose). Please see the repository’s LICENSE file for details.