#servidor
import socket
import threading

host = "127.0.0.1"
port = 6666
ThreadCount = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Creado")
sock.bind((host, port))
print ("socket bind completo")
sock.listen(1)
print ("socket escuchando ahora...")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('conexion con {}.'.format(addr))
        conn.send("server: Hola cliente".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('recibido: {}'.format(datos.decode('utf-8')))

            else:
                print("Sin conexion de cliente")
                break
    finally:
        conn.close()

while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
    ThreadCount += 1
    print('Numero de hilo: ' + str(ThreadCount))
    