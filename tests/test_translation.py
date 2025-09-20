import requests

BASE_URL = "http://127.0.0.1:5000/translate"

def test_translate_apple_es():
    response = requests.get(BASE_URL, params={"query": "apple", "locale": "es-ES"})
    assert response.status_code == 200
    assert response.json()["translation"] == "manzana"

def test_translate_banana_fr():
    response = requests.get(BASE_URL, params={"query": "banana", "locale": "fr-FR"})
    assert response.status_code == 200
    assert response.json()["translation"] == "banane"

def test_translate_missing_query():
    response = requests.get(BASE_URL, params={"locale": "es-ES"})
    assert response.status_code == 400

def test_translate_unknown_word():
    response = requests.get(BASE_URL, params={"query": "orange", "locale": "es-ES"})
    assert response.status_code == 404
    assert response.json()["translation"] == "N/A"
