# Classe &quot;JanelaConta&quot;:
from tkinter import *;
from conta import Conta;

janela = Tk()

janela.geometry('500x500+300+300')
janela.title('Conta')

ed_conta = Entry(janela, bg = 'white')
ed_conta.place(x = 155, y = 20)

ed_cli = Entry(janela, bg = 'white')
ed_cli.place(x = 155, y = 40)

ed_saldo = Entry(janela, bg = 'white')
ed_saldo.place(x = 155, y = 60)

ed_limite = Entry(janela, bg = 'white')
ed_limite.place(x = 155, y = 80)


lb = Label(janela, text = 'Conta:')
lb.place(x = 10, y = 20)

lb = Label(janela, text = 'Cliente:')
lb.place(x = 10, y = 40)

lb = Label(janela, text= 'Saldo:')
lb.place(x = 10, y = 60)

lb = Label(janela, text = 'Limite:')
lb.place(x = 10, y = 80)

lb = Label(janela, text = 'Valor:')
lb.place(x = 10, y = 150)

ed_valor = Entry(janela, bg = 'white')
ed_valor.place(x = 155, y = 150)

lb_m = Label(janela, text = '')
lb_m.place(x = 10, y=230)


def btn_click0():
    global c 
    if ed_saldo.get().isnumeric() and ed_limite.get().isnumeric():
        c = Conta(ed_conta.get(), ed_cli.get(), float(ed_saldo.get()), float(ed_limite.get()))
        lb_m['text'] = 'Conta criada com sucesso!' +c.mostraSaldo()
    else:
        lb_m['text'] = 'A conta não foi criada!'

def btn_click1():
    if ed_valor.get().isnumeric():
        c.depositar(float(ed_valor.get()))
        lb_m["text"] = "Depósito realizado com sucesso" + c.mostraSaldo()
    else:
        lb_m["text"] = "Valor inválido!!! Não é possível realizar a operação!!" + "Deposito não realizado!"

def btn_click2():
    if  ed_valor.get().isnumeric(): 
        if int(ed_valor.get()) > int(c.saldo + c.limite):
            lb_m["text"] = "Saque não realizado!"
        else:
            c.sacar(float(ed_valor.get()))
            lb_m["text"] = "Saque Realizado Com Sucesso" + c.mostraSaldo()  
    else:
        lb_m["text"] = "Valor inválido!!! Não é possível realizar a operação!!" + "Saque não realizado"

def btn_click3():
    lb_m['text'] = ''
    lb_m['text'] = c.mostraSaldo()


bt0 = Button(janela, text = 'Criar conta', width = 10, command = btn_click0)
bt0.place(x = 25, y = 200)

bt1 = Button(janela, text = 'Depositar', width = 10, command = btn_click1)
bt1.place(x = 120, y = 200)

bt2 = Button(janela, text = 'Sacar', width = 10, command = btn_click2)
bt2.place(x = 220, y = 200)

bt3 = Button(janela, text = 'Saldo', width = 10, command = btn_click3)
bt3.place(x = 320, y = 200)

janela.mainloop()