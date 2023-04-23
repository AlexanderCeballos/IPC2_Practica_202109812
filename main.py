from flask import jsonify, Flask, request
from flask_cors import CORS
import pila

app = Flask(__name__)
CORS(app)

pilaTemporal = pila.Pila()

@app.route('/postAgregarDatos', methods=['POST'])     
def addPila():
    if request.method == 'POST':
        valorLeido = request.form['dato']
        pilaTemporal.insertar(valorLeido)
        return jsonify({"Mensaje": "Dato agregado exitosamente"})

@app.route('/postCrearImagenPila', methods=['POST'])  
def agregar():
    return jsonify({"Se genero la imagen de la pila": str(pilaTemporal.generarDot())})

@app.route('/getValoresPila', methods = ['GET'])  
def getPila():
    return jsonify({"Pila": pilaTemporal.printPila()})

@app.route('/getCodigoImagenB64', methods=['GET'])  
def obtenerImagenB64():
    return jsonify({"Imagen de la pila": pilaTemporal.obtenerBase64()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)