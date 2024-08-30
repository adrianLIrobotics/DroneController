import keyboard
import requests

hostname = "raspberrypi"

# IP: 192.168.0.27 (LAN) RASPBERRY
url = 'http://'+hostname+':5000/pad_control'

# Función para enviar la solicitud con la tecla presionada
def send_key_request(key):
    try:
        # Enviar solicitud GET con el parámetro 'key'
        response = requests.get(url, params={'key': key})
        
        # Imprimir la respuesta del servidor
        if response.status_code == 200:
            print(f"Movimiento enviado: {response.json()['movement']}")
        else:
            print("Error en la solicitud")
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")

# Función para manejar las teclas presionadas
def on_key_event(event):
    key = event.name
    send_key_request(key)

# Configurar eventos para las teclas 'w', 'a', 's', 'd'
keyboard.on_press_key('w', on_key_event)
keyboard.on_press_key('a', on_key_event)
keyboard.on_press_key('s', on_key_event)
keyboard.on_press_key('d', on_key_event)

# Mantener el script corriendo
print("Presiona 'w', 'a', 's', 'd' para controlar el robot. Presiona 'esc' para salir.")
keyboard.wait('esc')
