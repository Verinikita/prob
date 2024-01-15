from flask import Flask, render_template, request, send_from_directory
import os
from zipfile import ZipFile

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
JSON_FOLDER = 'archivos_json'
PDB_FOLDER = 'archivos_pdb'
# Asegúrate de que las carpetas existan o créalas automáticamente
for folder in [UPLOAD_FOLDER, JSON_FOLDER, PDB_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def aplicar_funcion(zip_path):
    # Tu lógica para aplicar la función a los archivos ZIP
    # Aquí estoy simulando la extracción de archivos json y pdb
    with ZipFile(zip_path, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename.endswith(".json"):
                zip_info.filename = os.path.basename(zip_info.filename)
                fz.extract(zip_info, JSON_FOLDER)
            elif zip_info.filename.endswith(".pdb"):
                zip_info.filename = os.path.basename(zip_info.filename)
                fz.extract(zip_info, PDB_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'Error: No se ha proporcionado ningún archivo'

    file = request.files['file']

    if file.filename == '':
        return 'Error: No se ha seleccionado ningún archivo'

    if file and file.filename.endswith(".zip"):
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(zip_path)
        aplicar_funcion(zip_path)
        return 'Función aplicada con éxito'

    return 'Error: El archivo debe tener extensión .zip'

@app.route('/download/<folder_name>')
def download_folder(folder_name):
    zip_filename = f"{folder_name}.zip"
    zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)

    with ZipFile(zip_path, 'w') as zipf:
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

    return send_from_directory(app.config['UPLOAD_FOLDER'], zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
