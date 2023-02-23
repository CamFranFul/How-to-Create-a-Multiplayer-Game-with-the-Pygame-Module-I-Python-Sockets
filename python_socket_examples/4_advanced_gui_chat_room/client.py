# client side GUI Chat Room
import tkinter, socket, threading, json
from tkinter import DISABLED, VERTICAL, END, NORMAL, StringVar


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
white = "#ffffff"
red= "#ff3855"
orange = "#ffaa1d"
yellow = "#fff700"
green = "1fc742"
blue = "#5dadec"
purple = "#9c51b6"
root.config(bg=black)



class Connection():
    "A class to store a connection - a client socket and pertinent information"
    def __init__(self):
        self.encoder = "utf-8"
        self.bytesize = 1024
# define functions
def connect(connection):
    """Connect to a server at a given ip/port address"""
    # clear any previous chats
    my_listbox.delete(0, END)

    # we can append attributes to the 'Connection()' class by passing in a 'Connection()' obj. as an attribute for this function
    # I feel as if the 'connect_button' should be disabled until all 3 fields are filled in; otherwise,we should do a try & except block
    # get required info for connection from input fields
    connection.name = name_entry.get()
    connection.target_ip = ip_entry.get() # 192.168.1.247 is local IP address for this computer
    connection.port = port_entry.get()
    connection.color = color.get() # choose your color ahead of time before you connect

    try:
        # create a client socket
        connection.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.client_socket.connect((connection.target_ip, int(connection.port)))

        # receive an incoming message packet from the server
        message_json = connection.client_socket.recv(connection.bytesize) # bytes obj. of string rep of dict.
        process_message(connection, message_json)
    except:
        my_listbox.insert(0, "Connection not established...Goodbye.") # insert at beginning of chat history


def disconnect(connection):
    """Disconnect the client from the server"""
    pass

def gui_start():
    """Officially start connection by updating GUI by enabling and disabling widgets"""
    # buttons
    connect_button.config(state=DISABLED)
    disconnect_button.config(state=NORMAL)
    send_button.config(state=NORMAL)
    # entries
    name_entry.config(state=DISABLED)
    ip_entry.config(state=DISABLED)
    port_entry.config(state=DISABLED)
    # radio buttons
    for button in color_buttons:
        button.config(state=DISABLED)
def gui_end():
    """Officially end connection by updating the GUI"""
    pass

def create_message(flag, name, message, color):
    """Return a message packet to be sent"""
    message_packet = {
        "flag": flag,
        "name": name,
        "message": message,
        "color": color
    }

    return message_packet
def process_message(connection, message_json):
    """Update the client based on message packet flag"""
    message_packet = json.loads(message_json) # decode and turn to dict. in one step!
    flag = message_packet["flag"]
    name = message_packet["name"]
    message = message_packet["message"]
    color = message_packet["color"]

    if flag == "INFO":
        # Server is asking for information to verify connection. Send the info.
        message_packet = create_message("INFO", connection.name, f"{connection.name} Joins the server!", connection.color) # I added "f'{name} joins the server!"" for the message instead
        message_json = json.dumps(message_packet)
        connection.client_socket.send(message_json.encode(connection.encoder))

        # enable GUI for chat by enabling and disabling widgets
        gui_start()

        # create a thread to continuously receive messages from the server
        receive_thread = threading.Thread(target=receive_message, args=(connection,))
        receive_thread.start()

    elif flag == 'MESSAGE':
        pass

    elif flag == 'DISCONNECT':
        pass

    else:
        # catch for errors...
        my_listbox.insert(0, "Error processing message...") # insert at beginning of chat history


def send_message(connection):
    "Send a message to the server"
    pass

def receive_message(connection):
    """Receive a message from the server"""
    pass






# define GUI layout
# create frames: (info on top, color 2nd, output 3rd, and input on bottom)
info_frame = tkinter.Frame(root, bg=black) # for the user to input thier name along with the ip address and port of the server the user wants to connect to
color_frame = tkinter.Frame(root, bg=black) # for the row of color radio buttons that will allow the client/user to change the color of their message
output_frame = tkinter.Frame(root, bg=black) # to display the sent messages
input_frame = tkinter.Frame(root, bg=black) # for the user to input and send their message

# place the frames onto the root window via the pack system
info_frame.pack()
color_frame.pack()
output_frame.pack(pady=10) # output frame will take up the majority of the root window space
input_frame.pack()


# info frame layout
name_label = tkinter.Label(info_frame, text="Client Name:", font=my_font, fg=light_green, bg=black)
name_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=my_font, fg=light_green, bg=black)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tkinter.Label(info_frame, text="Port Num:", font=my_font, fg=light_green, bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10, command=lambda:connect(my_connection)) # button calls connect() function when pressed; my button is white instead of light green #     # I feel as if the 'connect_button' should be disabled until all 3 fields are filled in; otherwise,we should do a try & except block
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

# color frame layout
color = StringVar() # 'StringVar()' is a class imported from tkinter module that's a type of variable with objects that are strings such as 'color'
color.set(white) # sets 'color' to the value white by default
# these widgets will track the string variable object 'color'
# the value of this string variable object is expressed as a string, in this case colors are defined as strings
# 'variable = color' links these radio buttons to the variable 'color' based on what the 'value' variable is = to
white_button = tkinter.Radiobutton(color_frame, width=7, text="White", variable=color, value=white, bg=black, fg=light_green, font=my_font)
red_button = tkinter.Radiobutton(color_frame, width=7, text="Red", variable=color, value=red, bg=black, fg=light_green, font=my_font)
orange_button = tkinter.Radiobutton(color_frame, width=7, text="Orange", variable=color, value=orange, bg=black, fg=light_green, font=my_font)
yellow_button = tkinter.Radiobutton(color_frame, width=7, text="Yellow", variable=color, value=yellow, bg=black, fg=light_green, font=my_font)
green_button = tkinter.Radiobutton(color_frame, width=7, text="Green", variable=color, value=green, bg=black, fg=light_green, font=my_font)
blue_button = tkinter.Radiobutton(color_frame, width=7, text="Blue", variable=color, value=blue, bg=black, fg=light_green, font=my_font)
purple_button = tkinter.Radiobutton(color_frame, width=7, text="Purple", variable=color, value=purple, bg=black, fg=light_green, font=my_font)
color_buttons = [white_button, red_button, orange_button, yellow_button, green_button, blue_button, purple_button]

# place these radio button widgets onto the color frame via the grid system
white_button.grid(row=1, column=0, padx=2, pady=2)
red_button.grid(row=1, column=1, padx=2, pady=2)
orange_button.grid(row=1, column=2, padx=2, pady=2)
yellow_button.grid(row=1, column=3, padx=2, pady=2)
green_button.grid(row=1, column=4, padx=2, pady=2)
blue_button.grid(row=1, column=5, padx=2, pady=2)
purple_button.grid(row=1, column=6, padx=2, pady=2)

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




# create 'Connection()' class object and run the root window's mainloop()
my_connection = Connection()
root.mainloop() # calls the functions of the Tk() class