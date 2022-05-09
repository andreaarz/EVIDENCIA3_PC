import socket
import sys

def iniciar():
    # Inicializando el servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    s.bind(('127.0.0.1', 6543))
    s.listen(10)
    
    while True:
        # Se realiza el manejo de conexiones
        cliente, addr = s.accept()
        print('Conexion de: ', addr)

        chunks = []
        while True:
            # Administra los datos mientras el cliente manda mensaje.
            data = client.recv(2048)
            if not data:
            # Ya cuando el cliente termine de escribir.
                break
            chunks.append(data)
        cliente.sendall(b''.join(chunks))
        cliente.close()
        exit()
