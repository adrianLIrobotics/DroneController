'''
En RASPBERRY PI 3+
SERVIDOR EN DRONE
'''


from flask import Flask, jsonify, make_response, request
from flasgger import Swagger
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Generamos un servidor y lo levantamos
app = Flask(__name__)
Swagger(app)

# Definimos clase siguiendo metodologia OOP
class Dronecontrol:

    def __init__(self) -> None:
        
        # Configurar pines de control de dirección y PWM para el primer motor
        in1_1 = 24  # Pin de dirección 1 del primer motor
        in2_1 = 23  # Pin de dirección 2 del primer motor
        pwm_pin_1 = 7  # Pin PWM para controlar la velocidad del primer motor

        # Configurar pines de control de dirección y PWM para el segundo motor
        in1_2 = 16  # Pin de dirección 1 del segundo motor
        in2_2 = 15  # Pin de dirección 2 del segundo motor
        pwm_pin_2 = 11  # Pin PWM para controlar la velocidad del segundo motor

        # Configurar pines como salidas
        GPIO.setup(in1_1, GPIO.OUT)
        GPIO.setup(in2_1, GPIO.OUT)
        GPIO.setup(pwm_pin_1, GPIO.OUT)
        GPIO.setup(in1_2, GPIO.OUT)
        GPIO.setup(in2_2, GPIO.OUT)
        GPIO.setup(pwm_pin_2, GPIO.OUT)
        

        # Inicializar PWM en los pines seleccionados con una frecuencia más baja
        frequency = 1000  # Frecuencia en Hz (1 kHz)
        p1 = GPIO.PWM(pwm_pin_1, frequency)
        p2 = GPIO.PWM(pwm_pin_2, frequency)

        p1.start(0)
        p2.start(0)
        print("starting 0")
        time.sleep(3)

        # Configurar la dirección inicial para ambos motores (hacia adelante)
        GPIO.output(in1_1, GPIO.HIGH)
        GPIO.output(in2_1, GPIO.LOW)
        GPIO.output(in1_2, GPIO.HIGH)
        GPIO.output(in2_2, GPIO.LOW)

        p1.ChangeDutyCycle(3) # Empezar con un ciclo de trabajo bajo
        p2.ChangeDutyCycle(3) # Empezar con un ciclo de trabajo bajo

    def move_forward(self)->bool:
        i = 4
        # Mover hacia adelante con PWM ambos motores
        while i < 10:
            print(i)
            self.p1.ChangeDutyCycle(i)
            self.p2.ChangeDutyCycle(i) 
            time.sleep(0.05)
            i += 0.02

    def move_right(self)->bool:
        i = 4
        # Mover hacia adelante con PWM ambos motores
        while i < 10:
            print(i)
            self.p1.ChangeDutyCycle(0) # un motor no gira
            self.p2.ChangeDutyCycle(i)
            time.sleep(0.05)
            i += 0.02

    def move_left(self)->bool:
        i = 4
        # Mover hacia adelante con PWM ambos motores
        while i < 10:
            print(i)
            self.p1.ChangeDutyCycle(i) # un motor no gira
            self.p2.ChangeDutyCycle(0)
            time.sleep(0.05)
            i += 0.02

    def stop(self)->bool:
        self.p1.ChangeDutyCycle(0) # un motor no gira
        self.p2.ChangeDutyCycle(0) # un motor no gira

drone = Dronecontrol() # Generamos un objeto drone

# Este metodo escucha y cuando es llamado podemos acceder al contenido. Se trata 
# de un diccionario con clave Key y valor la tecla pulsada.
@app.route('/pad_control', methods=['GET'])
def generate_new_token():

    # Leer el parámetro 'key' que contiene la tecla pulsada
    key = request.args.get('key') # Obtenemos la tecla pulsada

    # Logica para mover el drone basado en la tecla pulsada

    if key == 'w':
        movement = "Avanzar"
        print("He recibido Avanzar")
        drone.move_forward() # Le pedimos al objeto drone que se mueva hacia delante.
       

    elif key == 'a':
        movement = "Girar a la izquierda"
        print("He recibido girar a la izquierda")
        drone.move_left()

    elif key == 'd':
        movement = "Girar a la derecha"
        print("He recibido derecha")
        drone.move_right()

    elif key == 'k':
        movement = "Parar"
        print("He recibido parar")
        drone.stop()

    else:
        movement = "Tecla no valida"
        print("He recibido Tecla no valida")

    # Responder con el movimiento asociado
    return jsonify({"movement": movement})


if __name__ == '__main__':
    # El server escucha al puerto 5000
    app.run(host='0.0.0.0', port=5000)
