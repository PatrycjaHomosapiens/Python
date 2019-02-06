# Zadanie 73_1

from tkinter import *
root = Tk()
root.title("Prosty interfejs GUI")
root.geometry("300x100")

app = Frame(root)
app.grid()
lbl = Label(app, text = "Szkolenie Python", bg = "red", font=("", 20), fg = "white", pady = "10")
lbl.grid()

# wprowadzanie przycisku
bttn1 = Button(app, text = "Przycisk pierwszy")
bttn1.grid()

# wprowadzanie przycisku - inna metoda
bttn2 = Button(app)
bttn2.grid()
bttn2["text"] = "Przycisk trzeci"







root.mainloop()