from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple translation dictionary
translations = {
    "apple": {"es-ES": "manzana", "fr-FR": "pomme", "de-DE": "Apfel"},
    "banana": {"es-ES": "plátano", "fr-FR": "banane", "de-DE": "Banane"},
}

@app.route("/translate")
def translate():
    query = request.args.get("query")
    locale = request.args.get("locale")

    if not query or not locale:
        return jsonify({"error": "Missing query or locale"}), 400

    translated = translations.get(query, {}).get(locale)
    if translated:
        return jsonify({"translation": translated})
    else:
        return jsonify({"translation": "N/A"}), 404

if __name__ == "__main__":
    app.run(debug=True)
