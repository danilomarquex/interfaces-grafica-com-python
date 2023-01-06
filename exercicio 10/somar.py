def Somar():
    n1 = int(numero01.get())
    n2 = int(numero02.get())
    mostrar['text'] = n1 + n2

from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('SOMA')

numero01 = Entry()
numero01.grid(row = 0, column = 0)

numero02 = Entry()
numero02.grid(row = 1, column = 0)

Button(text = 'SOMAR', command = Somar).grid(row=2, column = 0)

mostrar = Label(text = 'Resultado')
mostrar.grid(row = 3, column = 0)

root.mainloop()