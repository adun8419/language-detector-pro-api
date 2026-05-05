import requests

# Language Detector Pro
# Free API key: https://rapidapi.com/adunaev8419/api/language-detector-pro

API_KEY = "YOUR_RAPIDAPI_KEY"
BASE_URL = "https://language-detector-pro.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "Content-Type": "application/json"}

def detect_language(text):
    r = requests.post(f"{BASE_URL}/detect", json={"text": text}, headers=headers)
    return r.json()

def detect_batch(texts):
    r = requests.post(f"{BASE_URL}/batch", json={"texts": texts}, headers=headers)
    return r.json()

if __name__ == "__main__":
    print(detect_language("Bonjour le monde"))
    print(detect_language("Привет мир"))
    print(detect_batch(["Hello world", "Hola mundo", "こんにちは"]))