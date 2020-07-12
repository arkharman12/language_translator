from settings import *
from bottle import default_app, route, post, get, template, run, static_file, request, response

# Bottle-Autogenerator
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

# ---------Important files for local server-------
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=STATIC_ROOT)

@route('/media/<filepath:path>')
def server_media(filepath):
    return static_file(filepath, root=MEDIA_ROOT)

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root=STATIC_ROOT, download=filename)
#------------********---------------------

#Importing the google trans
from googletrans import Translator
translator = Translator()

#Main views
@route('/')
def index():
    translation = ""
    return template("index.html", translation=translation, lang="", name="")

@post('/')
def translateAction():
    # Gets data from textarea with name original
    originalText = request.forms.get('original')

    # Gets data from select dropdown
    destinationLang = request.forms.get('lang')

    # Runs custom translate function
    translation = translate(originalText, destinationLang)
    return template("index.html", translation=translation, lang=destinationLang, name=originalText)

#Translator
def translate(content, lang="", name=""):
    trans = translator.translate(content, dest=lang)
    return trans.text


application = default_app()
run(debug=DEBUG, reloader=True, host=HOST, port=PORT)
