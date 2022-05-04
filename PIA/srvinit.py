import socket
class client():
    def __init__(self):
        self.host = "127.0.0.1"  # The server's hostname or IP address
        self.port = 65432  # The port used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.bind(('', 8888))
            self.s.listen()
            print('El servidor está comenzando ...')
            conn,address = self.s.accept()
            self.s.connect((self.host, self.port))

            
    def run(self):
        conn, addr = self.s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
