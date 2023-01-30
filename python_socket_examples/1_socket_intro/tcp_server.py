# TCP Server Side

import socket

# create a server side socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# see how to get IP address dynamically
print(socket.gethostname()) # hostname
print(socket.gethostbyname(socket.gethostname())) # IP address of the given host name

# bind our new socket to a tuple (IP Address, Port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# put the socket into listening mode to listen for any possible connections
server_socket.listen()

# listen forever to accept ANY connection
while True:
    # accept every single connection and store two pieces of information
    client_socket, client_address = server_socket.accept() # returns a tuple of a client socket object and a tuple of that client socket object's IPv4 and port address that the client is using for the connection (the client port address being different from the server port address that he client is connecting to)
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)

    print(f'Connected to {client_address}!\n')

    # send a message to the client that just connected
    client_socket.send('You are connected!'.encode("utf-8"))

