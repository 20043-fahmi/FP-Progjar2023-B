import tkinter as tk
from tkinter import ttk
import socket
import threading
from tkinter import *
from PIL import Image, ImageTk
from feature.game import Game
from feature.chat import ChatPage


class Dashboard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Dashboard")
        self.img = Image.open("bg.png")
        self.bglabel = ImageTk.PhotoImage(self.img)
        ttk.Label(self, image=self.bglabel).place(x=0, y=0, relheight=1, relwidth=1)
        # bg = PhotoImage(file = "bg.png")
        # self.bglabel = Label(self, image = bg)
        # self.bglabel.place(x = 0, y = 0)
        # Labels
        self.my_frame = Frame(self, bg='#1B1E4D')
        self.my_frame.pack(pady=200)
        
        self.email_label = tk.Label(self.my_frame, text="Email:")
        self.email_label.grid(row=0, column=0, pady=10)
        
        self.username_label = tk.Label(self.my_frame, text="Username:")
        self.username_label.grid(row=2, column=0, pady=10)
        
        # Input fields
        self.email_entry = tk.Entry(self.my_frame)
        self.email_entry.grid(row=1, column=0, pady=5)
        
        self.username_entry = tk.Entry(self.my_frame)
        self.username_entry.grid(row=3, column=0, pady=5)
        # Submit button
        self.submit_button = tk.Button(
            self.my_frame, text="Submit", command=self.start_game_and_chat)
        self.submit_button.grid(row=4, column=0, pady=10)
        
        # Socket initialization
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        self.send_thread = threading.Thread(target=self.send_message)
        self.receive_thread = threading.Thread(target=self.receive_message)

    def start_game_and_chat(self):
        email = self.email_entry.get()
        username = self.username_entry.get()

        # Destroy current widgets in the dashboard
        self.email_label.destroy()
        self.email_entry.destroy()
        self.username_label.destroy()
        self.username_entry.destroy()
        self.submit_button.destroy()
        self.my_frame.destroy()
        # ttk.Label.destroy()
        # self.bglabel.destroy()
        # self.img.destroy()

        # Create game and chat components
        self.game = Game(self, username, email)
        self.chat = ChatPage(self, self.client_socket)

        # Positioning game and chat components side by side
        self.game.grid(row=0, column=0, padx=315, pady=20)
        self.chat.grid(row=1, column=0, padx=315, pady=20)

        # Start the game and chat
        self.send_thread.start()
        self.receive_thread.start()

    def send_message(self, event=None):
        message = self.chat.input_entry.get()
        if message and event is None:
            self.chat.display_message("You: " + message)
            self.client_socket.send(message.encode())
            self.chat.input_entry.delete(0, 'end')

    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            self.chat.display_message(message)


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.geometry("1280x768")  # Set the size of the dashboard window
    dashboard.mainloop()
