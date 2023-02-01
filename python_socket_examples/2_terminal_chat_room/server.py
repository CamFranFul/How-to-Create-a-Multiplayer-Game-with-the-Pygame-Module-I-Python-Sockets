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
client_socket_list = []
client_name_list = []

def broadcast_message(message):
     '''Send a message to All clients connected to the server'''
     pass
def receive_message(client_socket):
    '''Receive an incoming message from a specific client and forward the message to be broadcast'''

def connect_client():
    '''Connect an incoming client to the server'''
    while True:
        # Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        # send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        # add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # update the server, individual client, and ALL clients
        print(f"Name of new client is {client_name}\n") # server
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER))
        broadcast_message(f"{client_name} has joined the chat".encode(ENCODER))

# start the server
print("server is listening for incoming connection...")
connect_client()
# thread = threading.thread(target=connect_client)
# thread.start()



