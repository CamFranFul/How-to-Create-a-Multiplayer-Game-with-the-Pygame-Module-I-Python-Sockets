# chat server side
import socket

# define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# create a server socket, bind it to an ip/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()


# Accept any incoming connection and let them know they are connected
print("Server is running...\n")
client_socket, client_address  = server_socket.accept()
client_socket.send("You are connected to the server...\n".encode("UTF-8"))

# send/receive messages
while True:
    # receive information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    if message == "quit".lower():
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat...goodbye!")
        break
    else:
        print(f"\n{message}\n")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))
# close the socket
server_socket.close()