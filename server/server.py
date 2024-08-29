'''
En RASPBERRY PI 3+
http://localhost:5000/apidocs/
'''


from flask import Flask, jsonify, make_response, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/pad_control', methods=['GET'])
def generate_new_token():

    # Leer el parámetro 'key' que contiene la tecla pulsada
    key = request.args.get('key')

    # Logica para mover el robot basado en la tecla pulsada

    if key == 'w':
        movement = "Avanzar"
    elif key == 's':
        movement = "Retroceder"
    elif key == 'a':
        movement = "Girar a la izquierda"
    elif key == 'd':
        movement = "Girar a la derecha"
    elif key == 'k':
        movement = "Parar"
    else:
        movement = "Tecla no valida"

    # Responder con el movimiento asociado
    return jsonify({"movement": movement})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
