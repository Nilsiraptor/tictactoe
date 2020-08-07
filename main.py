from tkinter import *
from socket import *
from PIL import Image, ImageTk

# create window
root = Tk()
root.title("TicTacToe")
root.iconbitmap("Bilder/tictactoe.ico")

# add menu bar
menu = Menu(root)
root.config(menu=menu)

help_menu = Menu(menu)
menu.add_cascade(label="Hilfe", menu=help_menu)

# create window layout
status_bar = Label(root, text="Status", anchor="e", relief="sunken")
status_bar.pack(side="bottom", fill="x")

canvas = Canvas(root, width=400, height=400, relief="ridge", bd=2)
canvas.pack(side="left")

right_frame = Frame(root)
right_frame.pack(side="right", expand=True, fill="y")

ip_frame = Frame(right_frame, relief="ridge", bd=2)
ip_frame.pack(fill="x")

join_padding = Frame(right_frame, relief="ridge", bd=2)
join_padding.pack(fill="both")

join_frame = Frame(join_padding)
join_frame.pack(fill="both", padx=20, pady=20)

host_padding = Frame(right_frame, relief="ridge", bd=2)
host_padding.pack(fill="both")

host_frame = Frame(host_padding)
host_frame.pack(fill="both", padx=20, pady=20)

ip_text = Entry(ip_frame, justify="left", state="readonly", relief="flat")
ip_text.pack(side="right", fill="x")

ip_label = Label(ip_frame, text="Deine IP-Adresse:", anchor="e")
ip_label.pack(side="left", fill="x")
ip_label.pack_forget()

join_button = Button(join_frame, text="Beitreten", command=lambda: join_button.flash())
join_button.pack(side="bottom", fill="both")

join_entry = Entry(join_frame, justify="left")
join_entry.pack(side="right", fill="x")

join_label = Label(join_frame, text="IP-Adresse:", anchor="e")
join_label.pack(side="left", fill="x")

host_button = Button(host_frame, text="Host Server")
host_button.pack(fill="both")

start_button = Button(host_frame, text="Neues Spiel")
start_button.pack(fill="both")

board = PhotoImage(file="Bilder/tictactoe.gif")
canvas.create_image(200, 200, image=board)


root.mainloop()
