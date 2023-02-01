# client side chat room
import socket, threading

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP. DEST_PORT))

def send_message():
    '''send a message to the server to be broadcast'''
    pass

def receive_message():
    '''receive an incoming message from the server'''
    pass
