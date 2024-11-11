
import socket
import time

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Wait max 1 second
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Try connecting to a port
host = "localhost"
port = 80
is_open = check_port(host, port)
print(f"Port {port} is {'open' if is_open else 'closed'}")