import tkinter as tk
from tkinter import Tk, Button, Entry, StringVar

#1€ = 1.13USD =29333.00 Vietnamesischer Dong = 44,26 Türkische Lira

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Umrechner")
        self.root.geometry("300x300")

        # Label
        self.label = tk.Label(root, text="Geben Sie eine zahl in Euro ein")
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(root, text="USD", command=self.anzeigen)
        self.button.pack(pady=10)

         # Button_V
        self.button_V = tk.Button(root, text="Vietnamesischer Dong", command=self.anzeigen_V)
        self.button_V.pack(pady=10)

         # Button_T
        self.button_T = tk.Button(root, text="Türkische Lira", command=self.anzeigen_T)
        self.button_T.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def anzeigen(self):
        number = float(self.entry.get())
        number = number * 1.13
        self.output_label.config(text=f"Betrag: {round(number,2)} USD")

    def anzeigen_V(self):
        number_V = float(self.entry.get())
        number_V = number_V * 29333
        self.output_label.config(text=f"Betrag: {round(number_V,2)} VD")

    def anzeigen_T(self):
        number_T = float(self.entry.get())
        number_T = number_T * 44.26
        self.output_label.config(text=f"Betrag: {round(number_T,2)} Lira")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()

