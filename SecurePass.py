import tkinter as tk
from tkinter import messagebox
import re
import random
import string
from zxcvbn import zxcvbn  # Library for advanced password strength assessment
import os

class SecurePass:
    def __init__(self):
        self.criteria = {
            'length': (lambda pwd: len(pwd) >= 8, "Password must be at least 8 characters long."),
            'uppercase': (lambda pwd: any(c.isupper() for c in pwd), "Password must contain at least one uppercase letter."),
            'lowercase': (lambda pwd: any(c.islower() for c in pwd), "Password must contain at least one lowercase letter."),
            'numbers': (lambda pwd: any(c.isdigit() for c in pwd), "Password must contain at least one digit."),
            'special': (lambda pwd: any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in pwd), "Password must contain at least one special character.")
        }
        self.common_passwords = self.load_common_passwords()
    
    def load_common_passwords(self):
        # Load a list of common passwords from a file
        # This file should be included with your distribution or fetched from a secure source
        common_passwords = set()
        if os.path.exists('common_passwords.txt'):
            with open('common_passwords.txt') as f:
                for line in f:
                    common_passwords.add(line.strip())
        return common_passwords
    
    def assess_password(self, password):
        feedback = []
        score = 0

        # Check against common passwords
        if password in self.common_passwords:
            feedback.append("Password is too common.")
            return score, feedback

        for criterion, (check, message) in self.criteria.items():
            if check(password):
                score += 1
            else:
                feedback.append(message)

        return score, feedback

    def get_strength(self, score):
        if score == 5:
            return "Very Strong"
        elif score == 4:
            return "Strong"
        elif score == 3:
            return "Moderate"
        elif score == 2:
            return "Weak"
        else:
            return "Very Weak"

    def generate_password(self):
        length = random.randint(12, 16)
        password = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()-_=+[]{}|;:,.<>?/', k=length))
        return password

    def calculate_entropy(self, password):
        # Basic entropy calculation
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password):
            charset_size += len('!@#$%^&*()-_=+[]{}|;:,.<>?/')
        if charset_size == 0:
            return 0
        return len(password) * (charset_size.bit_length())

class SecurePassGUI:
    def __init__(self, root):
        self.secure_pass = SecurePass()
        self.root = root
        self.root.title("SecurePass: Password Strength Assessment Tool")

        self.password_label = tk.Label(root, text="Enter Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()
        self.password_entry.bind("<KeyRelease>", self.real_time_assessment)

        self.strength_label = tk.Label(root, text="")
        self.strength_label.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.suggestion_button = tk.Button(root, text="Generate Strong Password", command=self.generate_password)
        self.suggestion_button.pack()

        self.suggestion_label = tk.Label(root, text="")
        self.suggestion_label.pack()

        self.entropy_label = tk.Label(root, text="")
        self.entropy_label.pack()

        self.history = []

    def real_time_assessment(self, event):
        password = self.password_entry.get()
        score, feedback = self.secure_pass.assess_password(password)
        strength = self.secure_pass.get_strength(score)
        entropy = self.secure_pass.calculate_entropy(password)

        self.strength_label.config(text=f"Password Strength: {strength}")
        self.entropy_label.config(text=f"Entropy: {entropy} bits")

        if feedback:
            feedback_text = "Feedback:\n" + "\n".join(feedback)
        else:
            feedback_text = "Your password is strong!"
        self.feedback_label.config(text=feedback_text)

        self.history.append((password, strength, entropy))
        if len(self.history) > 10:
            self.history.pop(0)

    def generate_password(self):
        password = self.secure_pass.generate_password()
        self.suggestion_label.config(text=f"Suggested Password: {password}")

def main():
    root = tk.Tk()
    app = SecurePassGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
