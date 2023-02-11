# client side GUI Chat Room
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL, END, NORMAL


# define window
root = tkinter.Tk()
root.title("Chat Client")
root.iconbitmap("message_icon.png")
root.geometry("600x600")
root.resizable(0,0)


# define fonts and colors
my_font = ('SimSun', 14)
black = "#010101"
light_green = "#1fc742"
root.config(bg=black)

# define socket constants
ENCODER = 'utf-8'
BYTESIZE = 1024
global client_socket # 'global' means not restricted to one function; any changes made to this variable in a function will carry over to all the other functions as well


# define functions
def connect():
    """connect to a server at a given ip/port address"""
    global client_socket

    # clear any previous chats
    my_listbox.delete(0, END) # delete listbox contents from row index 0 to the last row index

    # get the required connection information
    # 'get()' function returns the input of an Entry class obj. in a string format
    name = name_entry.get()
    ip = ip_entry.get() # always a string and needs to be a string; 192.168.1.247 is local IP address for this computer
    port = port_entry.get() # always a string and needs to be an integer when sending

    # only try to make a connection if all 3 fields are filled in
    if name and ip and port:
        # conditions for connection are met, try for connection
        my_listbox.insert(0, f"{name} is waiting to connect to {ip} at {port}...") # '0' stands for index so insert this message at row '0' right at the top of the listbox

        # create a client socket to connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))  # must convert port address from string to integer       # try:
        #     client_socket.connect((ip, int(port))) # must convert port address from string to integer
        # except ConnectionRefusedError:
        #     # no name flag was sent, connection was refused # I would say 'connection invalid' instead because if there is no connection to the server to begin with, the server wouldn't be able to refuse a connection most likely due to an improper IP address
        #     my_listbox.insert(END, "connection invalid. Goodbye...")
        #     client_socket.close()

        # verify that the connection is valid
        verify_connection(name)
    else:
        # conditions for connection were not met
        my_listbox.insert(0, "Insufficient information for connection...") # '0' stands for index so insert this message at row '0' right at the top of the listbox


def verify_connection(name):
    """verify that the server connection is valid and pass required information"""
    global client_socket

    # the server will send a NAME flag if a valid connection is made
    flag = client_socket.recv(BYTESIZE).decode(ENCODER) # the string "NAME"

    if flag == 'NAME':
        # the connection was made, send client name and await verification
        client_socket.send(name.encode(ENCODER))
        message = client_socket.recv(BYTESIZE).decode(ENCODER) # "[name], you have connected to the server!"

        if message:
            # server sent a verification, connection is valid!
            my_listbox.insert(0, message)


            #change button states
            connect_button.config(state=DISABLED)
            disconnect_button.config(state=NORMAL) # 'NORMAL' instead of 'ENABLED' I guess b/c turned on by default
            send_button.config(state=NORMAL) # 'NORMAL' instead of 'ENABLED' I guess b/c turned on by default

            # change entry states
            name_entry.config(state=DISABLED)
            ip_entry.config(state=DISABLED)
            port_entry.config(state=DISABLED)

            # create a thread to continuously receive messages from the server
            receive_thread = threading.Thread(target=receive_message)
            receive_thread.start()
        else:
            # no verification message was received
            my_listbox.insert(END, "connection not verified. Goodbye...") # insert this message at last row index (bottom) of the listbox, must be b/c the server did not receive the client's inputted string properly
    else:
        # no name flag was sent, connection was refused # I would say 'connection invalid' instead because if there is no connection to the server to begin with, the server wouldn't be able to refuse a connection most likely due to an improper IP address
        my_listbox.insert(END, "connection invalid. Goodbye...")
        client_socket.close()
def disconnect():
    "disconnect from the server"
    global client_socket

    # close the socket
    client_socket.close()

    # change button states
    connect_button.config(state=NORMAL)
    disconnect_button.config(state=DISABLED)  # 'NORMAL' instead of 'ENABLED' I guess b/c turned on by default
    send_button.config(state=DISABLED)  # 'NORMAL' instead of 'ENABLED' I guess b/c turned on by default
    # change entry states
    name_entry.config(state=NORMAL)
    ip_entry.config(state=NORMAL)
    port_entry.config(state=NORMAL)

def send_message():
    """send a message to the server to be broadcast"""

    # send the message to the server
    message = input_entry.get() # what the user types in the input entry in the input frame
    client_socket.send(message.encode(ENCODER))

    # clear the input entry
    input_entry.delete(0, END)


def receive_message():
    """receive an incoming message from the server"""
    global client_socket

    while True:
        try:
            # receive an incoming message from the server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            my_listbox.insert(0, message)
        except:
            # an error occured, disconnect from the server
            my_listbox.insert(0, "Closing the connection. Goodbye...")
            disconnect()
            break



# define GUI layout
# create frames: (info on top, output in middle, and input on bottom)
info_frame = tkinter.Frame(root, bg=black) # for the user to input thier name along with the ip address and port of the server the user wants to connect to
output_frame = tkinter.Frame(root, bg=black) # to display the sent messages
input_frame = tkinter.Frame(root, bg=black) # for the user to input and send their message

# place the frames onto the root window via the pack system
info_frame.pack()
output_frame.pack(pady=10) # output frame will take up the majority of the root window space
input_frame.pack()


# info frame layout
name_label = tkinter.Label(info_frame, text="Client Name:", font=my_font, fg=light_green, bg=black)
name_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=my_font, fg=light_green, bg=black)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tkinter.Label(info_frame, text="Port Num:", font=my_font, fg=light_green, bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10, command=connect) # button calls connect() function when pressed; my button is white instead of light green
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5, width=10, state=DISABLED, command=disconnect) # disable disconnect button until a valid connection has been established; my button is white instead of light green

# place the widgets onto the info frame via the grid system
name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)



# output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame, orient=VERTICAL) # define scroll bar to scroll through sent messages
my_listbox = tkinter.Listbox(output_frame, height=20, width=55, borderwidth=3, bg=black, fg=light_green, yscrollcommand=my_scrollbar.set) # I guess don't have to put parenthesis when call functions in class attributes; the container that holds the sent messages
my_scrollbar.config(command=my_listbox.yview) # to synchronize the scroll bar with the listbox so that the scroll bar changes the vertical view of the listbox

# place the widgets onto the output frame via the grid system
my_listbox.grid(row=0, column=0) # don't know why the outline of the listbox is not showing up like in the tutorial
my_scrollbar.grid(row=0, column=1, sticky="NS") # sticky='NS' expands the scroll bar north and south (stretches it in both directions)




# input frame layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tkinter.Button(input_frame, text="send", borderwidth=5, width=10, font=my_font, bg=light_green, state=DISABLED, command=send_message) # disable send button until a valid connection has been established; my button is white instead of light green

# place the widgets onto the input frame via the grid system
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)




# run the root window's mainloop()
root.mainloop() # calls the functions of the Tk() class