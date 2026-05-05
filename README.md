# Language Detector Pro API

Detect language of any text. 100+ languages, confidence score, batch support.

**RapidAPI:** https://rapidapi.com/adunaev8419/api/language-detector-pro

## Quick Start

```python
import requests

url = "https://language-detector-pro.p.rapidapi.com/detect"
headers = {"X-RapidAPI-Key": "YOUR_KEY", "Content-Type": "application/json"}
r = requests.post(url, json={"text": "Bonjour le monde"}, headers=headers)
print(r.json())
# {"detected_language": "fr", "language_name": "French", "confidence": 0.98}
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /detect | POST | Single text detection |
| /batch | POST | Batch up to 100 texts |

## Pricing

| Plan | Price | Requests/hr |
|------|-------|-------------|
| BASIC | Free | 50 |
| PRO | $9.99/mo | 1,000 |
| ULTRA | $24.99/mo | 8,000 |

See `examples/` for Python, JavaScript, cURL samples.