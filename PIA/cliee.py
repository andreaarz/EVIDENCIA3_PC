import socket
import time

time.sleep(3)
# Creando Socket y estableciendo conexion.
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 6543))

# Mandando mensajes al server.
client_sock.sendall(b'Conexion completada.')
client_sock.shutdown(socket.SHUT_WR)

# Algoritmo para tomar los datos.
chunks = []
while True:
    data = client_sock.recv(2048)
    if not data:
        break
    chunks.append(data)
print('Mensaje recibido: ', repr(b''.join(chunks)))

# Desconectarse del server.
client_sock.close()
