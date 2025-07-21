from requests.exceptions import RequestException
import requests

def crawl(url: str) -> str:
    API_TOKEN = "<Crawlbase Normal requests token>"
    API_ENDPOINT = "https://api.crawlbase.com/"

    params = {
        "token": API_TOKEN,
        "url": url
    }

    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()

    return response.text
