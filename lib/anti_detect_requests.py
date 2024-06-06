import requests
from bs4 import BeautifulSoup
import random
import time

class AntiDetectRequests:
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
            # Add more user agents as needed
        ]
    
    def get(self, url, **kwargs):
        headers = self._get_headers()
        response = self.session.get(url, headers=headers, **kwargs)
        # response.raise_for_status()
        time.sleep(random.uniform(1, 3))  # Random sleep to mimic human behavior
        return response
    
    def bs4(self, url, **kwargs):
        response = self.get(url, **kwargs)
        return BeautifulSoup(response.content, 'html.parser')

    def _get_headers(self):
        user_agent = random.choice(self.user_agents)
        headers = {
            'User-Agent': user_agent,
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        return headers
