import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT=55857
s.bind(("", PORT))
print("Conexion UDP desde el puerto",PORT,".....")
 
while True:
    data, addr = s.recvfrom(1024)
    print("Recibido desde:  %s:%s" % addr)
    if data == b"salir":
        s.sendto(b"Hasta luego!\n", addr)
        continue
    s.sendto(b"Hola %s!\n" % data, addr)