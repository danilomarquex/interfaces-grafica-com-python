from tkinter import *
class Ip:
    def __init__(self, ip):
        self.ip = ip

    def validar(self):
        encontrou = True
        ip = tr01.get()
        ip = ip.split('.')
        for x in ip:
            if int(x) > 255 or len(ip) != 4:
                encontrou = False
                break
        return encontrou

    def testar(self):
        if self.validar() == True:
            lb02['text'] = 'VÁLIDO!!!'
        else:
            lb02['text'] = 'INVÁLIDO!!'


# JANELA!!

jip = Tk()
jip.geometry('250x200')
jip.resizable(False, False)

# Label 01
lb01 = Label(jip, text = 'Digite o endereço IP:')
lb01.pack()

# Entry
tr01 = Entry(jip)
tr01.pack()

# Instância
ip = Ip(tr01.get())

# Button
bt01 = Button(jip, text = 'VALIDAR', command = ip.testar)
bt01.pack()

# Label 2
lb02 = Label(jip, text='')
lb02.pack()


jip.mainloop()