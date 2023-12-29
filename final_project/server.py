from machinetranslation import translator
from flask import Flask, render_template, request, jsonify

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    french_text = translator.TranslationEn.translate(text_to_translate)
    return jsonify({"translated_text": french_text})

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    english_text = translator.TranslationFr.translate(text_to_translate)
    return jsonify({"translated_text": english_text})

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)