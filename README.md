# DroneController

Se define una arquitectura cliente-servidor usando comunicacion wiffi entre un portatil y una raspberry pi 3B+, ordenador que equipa un dron. Se eligue la comunicacion wifi sobre el bluetooth debido a la limitacion de distancia de 10 m de bluetooth.

El codigo se dibido en dos scripts, cada uno se lanza en una maquina.

El cliente en el laptop de control del operador del drone. Recibe los comandos de teclas y mediante request http manda la informacion a un servidor en la PI.

El server en la PI3B lanza un servidor usando la libreria flask creando un endpoint al cual el cliente llama para informar del comando que desea que el dron ejecute. 
El control del server esta programado siguiendo OOP Object Oriented programming y las funciones y objetos simulan el drone y sus capacidades. 


