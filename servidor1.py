import socket 
HOST=""
PORT=1234
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
print("esperando conexion")
s.bind(HOST,PORT)
s.listen()
conn,addr=s.accept()
with conn:
    print(f"Conectado al cliente{addr}")
    while True:
        data=conn.recv(1024)
        if not data:
            break
        conn.sendall(data)