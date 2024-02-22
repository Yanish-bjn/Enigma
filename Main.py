import tkinter as tk
from tkinter import ttk
from Process import EnigmaMachine

class EnigmaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Enigma Machine")

        self.label = ttk.Label(master, text="Enter message:")
        self.label.pack()

        self.entry = ttk.Entry(master)
        self.entry.pack()

        self.encrypt_button = ttk.Button(master, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.pack()

        self.decrypt_button = ttk.Button(master, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.pack()

        self.result_label = ttk.Label(master, text="")
        self.result_label.pack()

        self.enigma = EnigmaMachine()


    def encrypt_message(self):
        original_message = self.entry.get()
        encrypted_message = self.enigma.encrypt_message(original_message)
        self.result_label.config(text=f"Encrypted message: {encrypted_message}")

    def decrypt_message(self):
        original_message = self.entry.get()
        decrypted_message = self.enigma.decrypt_message(original_message)
        self.result_label.config(text=f"Decrypted message: {decrypted_message}")


def main():
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()        
