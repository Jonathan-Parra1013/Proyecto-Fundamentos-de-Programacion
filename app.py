from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    dato = request.form.get('dato')
    resultado = main.mi_funcion(dato)
    return render_template('index.html', resultado=resultado)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

