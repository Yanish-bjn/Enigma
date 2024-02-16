import string

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

    def encrypt_message(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                encrypted_message += self.encrypt_char(char.upper())
            else:
                encrypted_message += char
        return encrypted_message

def main():
    enigma = EnigmaMachine()
    
    message = "HELLO"
    encrypted_message = enigma.encrypt_message(message)
    
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
