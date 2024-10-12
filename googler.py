import requests
from bs4 import BeautifulSoup
import urllib.parse

num_results = 10
time_period = 'm'



def google_query(query):
    query = urllib.parse.quote_plus(query)
    search_url = f"https://www.google.com/search?q={query}&num={num_results}&tbs=qdr:{time_period}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [g.find('a')['href'] for g in soup.find_all('div', class_='tF2Cxc')]
    return links

def google_search(query):
    html_content = google_query(query)
    return extract_links(html_content)

# Exemple d'utilisation
if __name__ == "__main__":
    query = 'random query bellec'
    links = google_search(query)
    print(links)
