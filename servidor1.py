#Importar el paquete socket
from socket import *

#Variable donde definimos la ip del servidor
#dejar vacio para que cualquier cliente pueda conectarse
HOST = ''
#Definir el puerto de escucha del servidor
PORT = 1234
#Definir el buffer de cuantos bytes se va a transmitir los mensajes
BUFSIZ = 1024
#Variable donde se encuentra el host y el puerto
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)#Inicialización del socket de tipo UDP
#Asociar el socket con el host y el puerto
tcpSerSock.bind(ADDR)
# Activar el puerto de escucha
tcpSerSock.listen()

#Crear una comunicacion entre el servidor y el cliente
while True:
    print('Esperando la conexion del cliente')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Conectado desde:{}'.format(addr))

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()# Personajes aceptados
        if data:
                print('recibido: {}'.format(data.encode('utf-8')))
        else:
                print("Sin conexion de cliente")
                break
        mensaje = "Hola desde el servidor"
        tcpCliSock.send(mensaje.encode())# Enviar personaje
    tcpCliSock.close()
tcpSerSock.close()#Cerrar puerto

