#Importar la libreria para usar sockets
import socket

#Inicializacion del socket de tipo UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Definir el puerto por el cual va a escuchar
PORT=55857
#Asociar el puerto y el host con el socket
s.bind(("", PORT))
#Mensaje de prueba 
print("Conexion UDP desde el puerto",PORT,".....")
#Crear una comunicacion entre servidor y cliente 
while True:
    data, addr = s.recvfrom(1024)
    print("Recibido desde:  %s:%s" % addr)
    if data == b"salir":
        s.sendto(b"Hasta luego!\n", addr)
        continue
    s.sendto(b"Hola %s!\n" % data, addr)
