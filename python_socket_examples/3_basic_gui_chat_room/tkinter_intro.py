# Tkinter introduction
import tkinter # why does this not import everything automatically within tkinter???
from tkinter import BOTH, StringVar, END

# define window
root = tkinter.Tk()
root.title("Let's Chat")
root.iconbitmap('blue_talk.png')
root.geometry('400x600')
root.resizable(0,0)

# define colors
root_color = "#535657" # R:83, G:86, B:87 that is Very dark grayish cyan
input_color = "#4f646f" # R:79, G:100, B:111 that is Very dark grayish blue
output_color = "#dee7e7" # R:222, G:231, B:231 that is Light grayish cyan
root.config(bg=root_color)

# define functions
def send_message():
    '''send the user's message to the output frame'''
    message_label = tkinter.Label(output_frame, text=message_entry.get(), fg=text_color.get(), bg=output_color, font=('Helvetica', 12))
    message_label.pack()

    # clear the entry field for the next message
    message_entry.delete(0, END)

# define GUI layout
# define frames (that are placed on the root window)
input_frame = tkinter.LabelFrame(root, bg=input_color) # bg stands for background
output_frame = tkinter.LabelFrame(root, bg=output_color) # bg stands for background
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

# define widgets (that are placed on the frames)
message_entry = tkinter.Entry(input_frame, text = "Enter a message", width=25, font=("Helvetica", 12)) # why doesn't the "Enter a message" text show within the messsage entry textbox??
send_button = tkinter.Button(input_frame, text="Send", command=send_message, bg=output_color)
message_entry.grid(row=0, column=0, columnspan =3, padx=10, pady=10)
send_button.grid(row=0, column=3, rowspan=2, padx=10, pady=10) # did not include "ipadx=20, ipady=5" as the button gets cut off

text_color = StringVar() # 'StringVar()' is a class imported from tkinter module that's a type of variable with objects that are strings such as 'text_color'
text_color.set("#ff0000") # sets 'text color' to the value red by default
# these widgets will track the string variable object 'text_color'
# the value of this string variable object is expressed as a string, in this case the strings are text colors
red_button = tkinter.Radiobutton(input_frame, text="Red", variable=text_color, value="#ff0000", bg=input_color)
green_button = tkinter.Radiobutton(input_frame, text="Green", variable=text_color, value="#00ff00", bg=input_color)
blue_button = tkinter.Radiobutton(input_frame, text="Blue", variable=text_color, value="#0000ff", bg=input_color)
# place these radio button widgets onto the input frame via the grid system
red_button.grid(row=1, column=0)
green_button.grid(row=1, column=1)
blue_button.grid(row=1, column=2)

# creates the "---Stored Messages---" header for the output messages
output_label = tkinter.Label(output_frame, text="---Stored Messages---", fg=input_color, bg=output_color, font=('Helvetica bold', 18))
output_label.pack(pady=15)
# run the loop window's mainloop()
root.mainloop()


