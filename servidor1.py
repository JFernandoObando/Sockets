from socket import *


HOST = ''
PORT = 1234
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)#Inicialización
tcpSerSock.bind(ADDR)
tcpSerSock.listen()# Puerto de escucha


while True:
    print('witing for connection')#Esperando la conexión del cliente
    tcpCliSock, addr = tcpSerSock.accept()
    print('connected from:{}'.format(addr))

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

