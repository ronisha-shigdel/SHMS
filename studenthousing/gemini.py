import requests
from django.conf import settings

def get_gemini_data():
    url = "https://api.gemini.com/v1/symbols"
    response = requests.get(url, auth=(settings.GEMINI_API_KEY, settings.GEMINI_API_SECRET))
    if response.status_code == 200:
        return response.json()
    else:
        return None