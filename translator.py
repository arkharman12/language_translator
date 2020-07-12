from googletrans import Translator
from bottle import default_app, route, template, post, request

# Example code
# translator = Translator()
# translator.translate('안녕하세요.')
# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='hi')
# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)

def home():
    return template("index.html")

def translate():
    content = request.forms.get("content")
    lang = request.forms.get("lang")
    t= translator.translate(content, dest= lang)
    return template("index.html", trans= t)
