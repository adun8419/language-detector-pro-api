const API_KEY = "YOUR_RAPIDAPI_KEY";
const BASE_URL = "https://language-detector-pro.p.rapidapi.com";

async function detectLanguage(text) {
  const res = await fetch(`${BASE_URL}/detect`, {
    method: "POST",
    headers: {"X-RapidAPI-Key": API_KEY, "Content-Type": "application/json"},
    body: JSON.stringify({ text })
  });
  return res.json();
}

detectLanguage("Привет мир").then(console.log);
// { detected_language: "ru", language_name: "Russian", confidence: 0.99 }