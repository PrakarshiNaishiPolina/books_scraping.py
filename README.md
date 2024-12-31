# Book Details Scraper

This Python script scrapes book details from the [Books to Scrape](http://books.toscrape.com/) website and saves the information to a text file named `books_details.txt`.

## Features

- **Scrapes Data**: Extracts book details including title, price, availability, and rating.
- **Parses HTML**: Utilizes `BeautifulSoup` to parse HTML content.
- **Saves Data**: Writes the scraped data to a text file for offline use.

## Prerequisites

Ensure you have the following libraries installed:
- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing and navigating HTML content.

Install them using pip if necessary:
```bash
pip install requests beautifulsoup4
