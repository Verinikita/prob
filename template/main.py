from flask import Flask, render_template, flash, redirect, url_for
from funct import uploader

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'home/verobaro/scTCR/PAGINA/downlo'
app.secret_key = 'clave_secreta'  # Necesario para usar 'flash'

@app.route("home/verobaro/scTCR/PAGINA/templates", methods=['POST'])
def main_uploader():
    # Llama a la función uploader
    result = uploader(request)

    # Haz algo con el resultado, por ejemplo, mostrarlo con flash
    flash(result)
    return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug=True)
