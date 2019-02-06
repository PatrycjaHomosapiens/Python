# Zadanie 73_2

from tkinter import *
root = Tk()
root.title("Prosty interfejs GUI")
root.geometry("300x100")

def wstawTest():
    lbl["text"] = "TEST"

app = Frame(root)
app.grid()

bttn1 = Button(app, text = "Wstaw TEST", command=wstawTest)  #
bttn1.grid()


lbl = Label(app, text = "...")
lbl.grid()



root.mainloop()