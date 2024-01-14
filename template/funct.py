from flask import Flask, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'zip'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploader(request):
    if 'zipFile' not in request.files:
        flash('No se ha proporcionado ningún archivo')
        return 'Error: No se ha proporcionado ningún archivo'

    file = request.files['zipFile']

    if file.filename == '':
        flash('No se ha seleccionado ningún archivo')
        return 'Error: No se ha seleccionado ningún archivo'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('./PAGINA/scTCR/PAGINA/downlo', filename))
        flash('Archivo subido exitosamente')
        return 'Archivo subido exitosamente'

    flash('El tipo de archivo no está permitido')
    return 'Error: El tipo de archivo no está permitido'
