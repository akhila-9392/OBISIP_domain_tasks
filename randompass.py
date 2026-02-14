import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # External library for clipboard integration

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure PassGen Pro")
        self.root.geometry("350x450")

        # 4. GUI Design: Layout and labels
        tk.Label(root, text="Password Length:", font=("Arial", 10)).pack(pady=10)
        self.length_slider = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL)
        self.length_slider.set(12)
        self.length_slider.pack()

        # Checkbuttons for Customization
        self.var_letters = tk.BooleanVar(value=True)
        self.var_numbers = tk.BooleanVar(value=True)
        self.var_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Letters", variable=self.var_letters).pack()
        tk.Checkbutton(root, text="Include Numbers", variable=self.var_numbers).pack()
        tk.Checkbutton(root, text="Include Symbols", variable=self.var_symbols).pack()

        # Generate Button
        tk.Button(root, text="Generate Password", command=self.create_pass, bg="#2196F3", fg="white").pack(pady=20)

        # Result Display
        self.result_entry = tk.Entry(root, font=("Courier", 12), justify='center', bd=2)
        self.result_entry.pack(pady=5, fill='x', padx=20)

        # 6. Clipboard Integration
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clip).pack(pady=10)

    def create_pass(self):
        # 5. Security Rules & Randomization
        length = self.length_slider.get()
        pool = ""
        if self.var_letters.get(): pool += string.ascii_letters
        if self.var_numbers.get(): pool += string.digits
        if self.var_symbols.get(): pool += string.punctuation

        if not pool:
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        password = "".join(random.SystemRandom().choice(pool) for _ in range(length))
        
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

    def copy_to_clip(self):
        password = self.result_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()