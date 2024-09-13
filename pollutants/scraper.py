# pollutants/scraper.py
import requests

#urllib is a module in a python for handing urls.
from urllib.request import urlopen
# Request module is used to send http requests.
import requests
#BeautifulSoap is used  to pulling out the data from html and xml files.
from bs4 import BeautifulSoup
#urllib.parse is used to break url string into components.
import urllib.parse
import os
#Defines a function called extract_article_text that takes a URL as input and
# returns the extracted title and article text.
def fetch_pollutant_data():
    try:
        url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract article title and text
        title = soup.title.text.strip() if soup.title else "No Title"

        # Identify the main content container (adjust as needed)
        content_container = soup.find('article') or soup.find('div', class_='main-content') or soup.body

        # Extract text only from relevant elements (e.g., paragraphs)
        article_text = ' '.join([p.text for p in content_container.find_all(['p', 'div'], recursive=False)])
        article_text = ' '.join(article_text.split())
        return title, article_text
    except Exception as e:
        print(f"Error extracting content from {url}: {str(e)}")
        return None, None



