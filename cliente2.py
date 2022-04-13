import socket #libreria para trabajar con sockets
 
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creacion de socket con parametros de UDP
addr = ("172.17.37.152", 55857) # Conecta el programa del servidor con la ip y puerto

#Enviar y recibir mensajes
while True:
    data = input("Ingresa tu nombre: ")
    if not data:
        continue 
    s_udp.sendto(data.encode(), addr) #envia el mensaje al servidor en bytes
    response, addr = s_udp.recvfrom(1024) #aceptar el mensaje del servidor
    print(response.decode()) #imprime el mensaje escrito
    if data == "salir":
        print("La sesion con el servidor a terminado %s:%s\n" % addr)
        break #sale del bucle

s_udp.close() #finalizacion del socket
