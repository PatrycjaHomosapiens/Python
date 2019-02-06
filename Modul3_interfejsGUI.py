# Interfejs GUI

from tkinter import *
root = Tk()
root.title("Prosty interfejs GUI")      # title to metoda, nawias to argument
root.geometry("225x100")

app = Frame(root)       # to jest dziedziczenie
app.grid()              # grid to uwidocznienie ramki
lbl = Label(app, text = "Jestem etykietą!")
lbl.grid()              # uwidocznienie etykiety








root.mainloop()     # to jest taka pętla (jak while True), dajemy to zawsze na końcu i tylko 1 raz