# Genshin Impact Character Scraper

This project is a FastAPI-based application that scrapes character data from the Genshin Impact Fandom website and serves it through an API. It also saves the data to a CSV file for further use.

## Features

- Scrapes Genshin Impact character data, including:
  - Icon URL
  - Name
  - Quality
  - Element
  - Weapon
  - Region
  - Model type
- Saves the scraped data to a CSV file (`genshin_characters.csv`).
- Provides an API endpoint to retrieve character data in JSON format.
- CORS middleware to allow cross-origin requests (e.g., for use with a frontend).

## Why We Chose Requests + BeautifulSoup for Scraping

We chose Requests and BeautifulSoup for web scraping because:

- **Requests**: Provides a simple and reliable way to make HTTP requests, handle responses, and manage errors.
- **BeautifulSoup**: Offers powerful and intuitive tools for parsing and navigating HTML, making it easy to extract the necessary data from web pages.
- These libraries are lightweight, well-documented, and widely used, making them ideal for building a robust and maintainable scraping solution.

## Analysis of the Site

- The site appears to be primarily based on static HTML, meaning the data is likely visible directly in the source code (no need for JavaScript rendering).
- Pages are well-structured, typical of wikis (tables, lists, etc.).

## Tool Recommendation

Given that the site does not seem to require complex JavaScript rendering, here are our recommendations:

### BeautifulSoup + Requests (Best Choice for This Case)

**Why:**

- The site appears static and well-structured.
- BeautifulSoup excels at extracting information from static HTML.

**Advantages:**

- Simple to set up.
- Perfect for extracting structured tables or lists, such as Genshin Impact character data.

## Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`
- `fastapi`
- `uvicorn`

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to:

   - API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - API endpoint: [http://127.0.0.1:8000/genshin_characters](http://127.0.0.1:8000/genshin_characters)

## Usage

### Scraping Data

The scraping functionality is handled by the `scrape_genshin_characters_to_csv` function. It:

1. Fetches the Genshin Impact character data from the specified URL.
2. Extracts relevant information from the webpage.
3. Saves the data into a CSV file (`genshin_characters.csv`).

By default, the URL used is:

```
https://genshin-impact.fandom.com/wiki/Characters
```

### API Endpoint

The `/genshin_characters` endpoint serves the character data from the CSV file in JSON format. If the CSV file is missing, the endpoint returns a 404 error with an appropriate message.

## Configuration

CORS middleware is configured to allow requests from:

```
http://localhost:3000
```

You can modify this in the `app.add_middleware` configuration section of the code if needed.

## CSV Output

The scraped data is saved to a CSV file (`genshin_characters.csv`) with the following columns:

- Icon URL
- Name
- Quality
- Element
- Weapon
- Region
- Model type

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.