import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

class BMICalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced BMI Tracker")
        self.root.geometry("300x400")

        # UI Elements
        tk.Label(root, text="Name:").pack(pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        tk.Label(root, text="Weight (kg):").pack(pady=5)
        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()

        tk.Label(root, text="Height (m):").pack(pady=5)
        self.entry_height = tk.Entry(root)
        self.entry_height.pack()

        tk.Button(root, text="Calculate & Save", command=self.process_bmi, bg="#4CAF50", fg="white").pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
        self.result_label.pack()

    def process_bmi(self):
        try:
            name = self.entry_name.get()
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            if not name:
                raise ValueError("Name is required")

            bmi = round(weight / (height ** 2), 2)
            
            # Simple Categorization logic
            status = "Obesity" if bmi >= 30 else "Overweight" if bmi >= 25 else "Normal" if bmi >= 18.5 else "Underweight"
            
            self.result_label.config(text=f"BMI: {bmi}\n({status})")

            # 5. Data Storage (CSV)
            self.save_to_file(name, weight, height, bmi, status)
            messagebox.showinfo("Success", "Data saved successfully!")

        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid data.")

    def save_to_file(self, name, w, h, bmi, status):
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("bmi_history.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, name, w, h, bmi, status])

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorGUI(root)
    root.mainloop()