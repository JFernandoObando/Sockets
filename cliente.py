import imp


import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=("localhost",65432)
while True:
    data=input("Ingrese el nombre del cliente")
    if not data:
        continue
    s.sendto(data.encode(),addr)
    response,addr=s.recvfrom(1024)
    print(response.decode)
    if data =="salir":
        print("La sesion con el servidor termino: ", addr)
        break
    s.close