# server side chat room
import socket, threading

# define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# create two blank lists to store connected client sockets and their names
client_sockets_list = []
client_name_list = []

def broadcast_message(message):
     '''Send a message to All clients connected to the server'''
     pass
def receive_message(client_socket):
    '''Receive an incoming message from a specific client and forward the message to be broadcast'''

def connect_client():
    '''Connect an incoming client to the server'''
    pass
