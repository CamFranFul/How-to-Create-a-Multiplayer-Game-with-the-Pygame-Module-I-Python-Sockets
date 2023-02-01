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
     # I feel as if there could be a socket function that broadcasts a message to all clients so we wouldn't need to create our own broadcast_message() function
     for client_socket in client_socket_list:
         client_socket.send(message)


def receive_message(client_socket, client_address): # I added 'client_address'
    '''Receive an incoming message from a specific client and forward the message to be broadcast'''
    while True:
        try:
            # get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # receive message from the client
            message = client_socket.recv(BYTESIZE).decode(ENCODER) # or can maybe do it like this as well?: message = (name + ":" + message).encode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER) # bright green, bolded message tabbed in
            broadcast_message(message)
        except:
            # find the index of the client socket in our lists
            # I don't understand why we have to redefine index and name seems redundant
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]


            # remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # close the client socket
            client_socket.close()

            # broadcast that the client has left the chat
            broadcast_message(f"\033[5;91m\t{name} has left the chat!\033[0m".encode(ENCODER)) # bright red, blinking message tabbed in
            print(f'{client_address} disconnected.') # I added this




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
        broadcast_message(f"\n{client_name} has joined the chat".encode(ENCODER))

        # now that a new client has connected, start a thread
        receive_thread = threading.Thread(target=receive_message, args=(client_socket, client_address,))
        receive_thread.start()

# start the server
print("server is listening for incoming connection...")
connect_client()
# thread = threading.thread(target=connect_client)
# thread.start()



