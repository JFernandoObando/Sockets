from socket import * #libreria para trabajar con sockets

HOST = '172.17.37.152' #declaracion de la ip del servidor
PORT = 1236 #declaracion del puerto
BUFSIZ = 1024 #tamaño del bufer en bytes
ADDR = (HOST, PORT) 

s_tcp = socket(AF_INET, SOCK_STREAM) #Creacion de socket con parametros de TCP
s_tcp.connect(ADDR)# Conecta el programa del servidor

#Enviar y recibir mensajes
while True:
    dato = input('Ingresa un mensaje: ')
    if not dato:
        break #dato vacio sale del bucle
    s_tcp.send(dato.encode('utf-8')) #envia el mensaje al servidor en bytes
    b_dato = s_tcp.recv(BUFSIZ).decode() #aceptar el mensaje del servidor
    if not b_dato:
        break #sin bytes sale del bucle
    print(b_dato) #imprime el mensaje del servidor
s_tcp.close() #finalizacion del socket
