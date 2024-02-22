import tkinter as tk
from tkinter import ttk


class EnigmaMachine:
    def __init__(self):
        self.rotors = [
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        self.reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.rotor_positions = [0, 0, 0]  # Initial positions of rotors

    def rotate_rotors(self):
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26

        if self.rotor_positions[0] == self.rotors[0].index('R'):  # Check for turnover of the first rotor
            self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26

            if self.rotor_positions[1] == self.rotors[1].index('F'):  # Check for turnover of the second rotor
                self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26

    def encrypt_char(self, char):
        self.rotate_rotors()

        # Input through rotors
        for i in range(3):
            char = self.rotors[i][(ord(char) - ord('A') + self.rotor_positions[i]) % 26]

        # Reflector
        char = self.reflector[ord(char) - ord('A')]

        # Output through rotors (in reverse order)
        for i in range(2, -1, -1):
            char = chr((self.rotors[i].index(char) - self.rotor_positions[i] + 26) % 26 + ord('A'))

        return char
    

    def decrypt_char(self, char):
        rotor = self.rotors[0]
        position = rotor.index(char)
        decrypted_position = (position - self.rotor_positions[0]) % len(rotor)
        return rotor[decrypted_position]

    def reset_rotors(self):
        self.rotor_positions = [0, 0, 0]

    def encrypt_message(self, message):
        self.reset_rotors()
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                self.rotate_rotors()
                encrypted_message += self.encrypt_char(char.upper())
            else:
                encrypted_message += char
        return encrypted_message
    
    def decrypt_message(self, message):
        self.reset_rotors()
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                self.rotate_rotors()
                decrypted_message += self.encrypt_char(char.upper())
            else:
                decrypted_message += char
        return decrypted_message
