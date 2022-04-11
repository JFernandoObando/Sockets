from socket import *

HOST = '172.17.37.152'
PORT = 1236
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    sdata = input('> ')
    tcpCliSock.send(sdata.encode('utf-8'))
    if not sdata:
        break
    tcpCliSock.send(sdata.encode())
    rdata = tcpCliSock.recv(BUFSIZ).decode()
    if not rdata:
        break
    print(rdata)
tcpCliSock.close()
