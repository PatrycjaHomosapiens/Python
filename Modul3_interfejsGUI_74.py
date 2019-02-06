# Zadanie 74
# zmienna globalna - to zmienna zdefiniowana poz

from tkinter import *
root = Tk()
root.title("Prosty interfejs GUI")
root.geometry("300x100")

liczbaKlikniec = 0

def klik():
    global liczbaKlikniec
    liczbaKlikniec += 1
    bttn1["text"] = "Liczba kliknięć: "+str(liczbaKlikniec)

app = Frame(root)
app.grid()

bttn1 = Button(app, text = "Liczba kliknięć: 0", command=klik)
bttn1.grid()




root.mainloop()