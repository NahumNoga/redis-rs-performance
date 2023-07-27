import socket  # Import socket module
import time

def start() -> None:
    host = socket.gethostname()
    port = 12345                   # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    large_data = bytearray(491520)
    large_data_bytes = bytes(large_data)
    s.sendall(large_data_bytes)
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))
