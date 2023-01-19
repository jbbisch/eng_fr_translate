import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    textToTranslate = request.args.get('textToTranslate')
    french_text = TranslationEn.translate(english_text) # Write your code here
    return "Translated text to French" french_text

@app.route("/french_to_english")
def french_to_english(french_text):
    textToTranslate = request.args.get('textToTranslate')
    english_text = TranslationFr.translate(french_text) # Write your code here
    return "Translated text to English" eglish_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
