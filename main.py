import tkinter as tk
import socket
import threading
from feature.game import Game
from feature.chat import ChatPage


class Dashboard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Dashboard")

        # Labels
        self.email_label = tk.Label(self, text="Email:")
        self.username_label = tk.Label(self, text="Username:")

        # Input fields
        self.email_entry = tk.Entry(self)
        self.username_entry = tk.Entry(self)

        # Submit button
        self.submit_button = tk.Button(
            self, text="Submit", command=self.start_game_and_chat)

        # Positioning labels, input fields, and button vertically centered
        self.email_label.pack(pady=10)
        self.email_entry.pack(pady=5)
        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=5)
        self.submit_button.pack(pady=10)
        
        # bg = tk.PhotoImage(file = "Your_img.png")

        # canvas1 = tk.Canvas( tk(), width = 1280, height = 720)
  
        # canvas1.pack(fill = "both", expand = True)
  
        # canvas1.create_image( 0, 0, image = bg, anchor = "nw")

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

        # Create game and chat components
        self.game = Game(self, username, email)
        self.chat = ChatPage(self, self.client_socket)

        # Positioning game and chat components side by side
        self.game.grid(row=0, column=0, padx=20, pady=20)
        self.chat.grid(row=0, column=1, padx=20, pady=20)

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
    dashboard.geometry("1280x720")  # Set the size of the dashboard window
    dashboard.mainloop()
