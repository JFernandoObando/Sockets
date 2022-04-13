#servidor
#Importar libreria para el uso de sockets
import socket
#Definir librerias para el uso de hilos
import threading
#Establecer el host vacio para que cualquier cliente pueda conectarse
host = ""
#Establecer el puerto de escucha del servidor
port = 6666
#Contador de hilos
ThreadCount = 0

#Iniciar el socket de tipo TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Creado")
#Conexion del socket con el host por el puerto establecido
sock.bind((host, port))
print ("socket bind completo")
#Socket escuchando a los clientes
sock.listen(1)
print ("socket escuchando ahora...")

#Definir una comunicacion entre servidor y clientes de tipo multihilo
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
    
