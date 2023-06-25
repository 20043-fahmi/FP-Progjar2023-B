import tkinter as tk
import socket
import threading
from feature.chat import ChatPage
from feature.game import Game


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main Window")

        self.game = Game(self)
        self.chat = ChatPage(self)

        self.game.grid(row=0, column=0, padx=20, pady=20)
        self.chat.grid(row=0, column=1, padx=20, pady=20)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        self.send_thread = threading.Thread(target=self.send_message)
        self.receive_thread = threading.Thread(target=self.receive_message)

        self.send_thread.start()
        self.receive_thread.start()

    def send_message(self):
        while True:
            message = self.chat.input_entry.get()
            if message:
                self.client_socket.send(message.encode())

    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            self.chat.display_message(message)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
