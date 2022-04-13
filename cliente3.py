import socket #libreria para trabajar con sockets

host = "172.17.37.152" #declaracion de la ip del servidor
port = 6666 #declaracion del puerto

sock = socket.socket() #objeto socket no bloqueante

sock.connect((host, port)) # Conecta el programa del servidor

datos = sock.recv(4096) #aceptar el mensaje del servidor
print (datos.decode('utf-8')) #imprime el mensaje

#Enviar mensaje
while True:

  message = input("envia un mensaje: ")
  sock.send(message.encode('utf-8')) #envia el mensaje al servidor en bytes

  if message == "salir":
        print("bye") 
        break #sale del bucle

sock.close() #finalizacion del socket
