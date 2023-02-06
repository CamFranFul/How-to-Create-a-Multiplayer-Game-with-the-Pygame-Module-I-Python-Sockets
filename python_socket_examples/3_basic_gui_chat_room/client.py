# client side GUI Chat Room
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL

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

# define functions
def connect():
    """connect to a server at a given ip/port address"""
    pass


def verify_connection():
    """verify that the server connection is valid"""
    pass





def disconnect():
    "disconnect from the server"
    pass

def send_message():
    """send a message to the server to be broadcast"""
    pass


def recieve_message():
    """receive an incoming message from the server"""
    pass



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
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5, width=10, state=DISABLED) # disable disconnect button until a valid connection has been established

# place the widgets onto the frame via the grid system
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
my_scrollbar.config(command=my_listbox.yview) # to synchronize the scroll bar with the lsitbox so that the scroll bar changes the vertical view of the listbox

# place the widgets onto the frame via the grid system
my_listbox.grid(row=0, column=0) # don't know why the outline of the listbox is not showing up like in the tutorial
my_scrollbar.grid(row=0, column=1, sticky="NS")




# input frame layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tkinter.Button(input_frame, text="send", borderwidth=5, width=10, font=my_font, bg=light_green, state=DISABLED) # disable send button until a valid connection has been established

# place the widgets onto the frame via the grid system
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)




# run the root window's mainloop()
root.mainloop()