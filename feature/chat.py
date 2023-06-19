import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class ChatPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Chat display area
        self.chat_display = ScrolledText(self, height=15, state='disabled')
        self.chat_display.pack(fill='both', expand=True)

        # User input area
        self.input_frame = tk.Frame(self, background='white')
        self.input_frame.pack(fill='x')

        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side='left', fill='x', expand=True)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text='Send', command=self.send_message)
        self.send_button.pack(side='right')

    def send_message(self, event):
        message = self.message_entry.get()
        self.message_entry.delete(0, 'end')
        self.display_message(message)

    def display_message(self, message):
        self.chat_text.configure(state='normal')
        self.chat_text.insert('end', message + '\n')
        self.chat_text.configure(state='disabled')
        self.chat_text.see('end')