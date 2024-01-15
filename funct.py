from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')



UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downl'
ALLOWED_EXTENSIONS = {'zip'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
        flash('Archivo subido exitosamente')
        return 'Archivo subido exitosamente'

    flash('El tipo de archivo no está permitido')
    return 'Error: El tipo de archivo no está permitido'
