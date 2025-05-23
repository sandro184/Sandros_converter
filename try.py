import tkinter as tk

def umrechnen():
    try:
        euro = float(eingabe.get())
        usd = euro * 1.13
        vnd = euro * 29333
        ausgabe.config(text=f"{usd:.2f} USD\n{vnd:.0f} VND")
    except:
        ausgabe.config(text="Ungültige Eingabe")

fenster = tk.Tk()
fenster.title("Währungsrechner")

tk.Label(fenster, text="Euro:").pack()
eingabe = tk.Entry(fenster)
eingabe.pack()

tk.Button(fenster, text="Umrechnen", command=umrechnen).pack()
ausgabe = tk.Label(fenster, text="")
ausgabe.pack()

fenster.mainloop()
