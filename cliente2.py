
import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 55857)
 
while True:
    data = input("Ingresa tu nombre: ")
    if not data:
        continue
    s.sendto(data.encode(), addr)
    response, addr = s.recvfrom(1024)
    print(response.decode())
    if data == "salir":
        print("La sesion con el servidor a terminado %s:%s\n" % addr)
        break
 
s.close()