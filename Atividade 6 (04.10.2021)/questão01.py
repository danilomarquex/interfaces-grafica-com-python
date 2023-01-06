from tkinter import *
class Aluno:
    def _init_(self,n,m,b):
        self.nome=n
        self.matricula=m
        self.bolsista=b
        self.mensalidade=400
    
    def calculaM(self):
        if self.bolsista==1:
            self.mensalidade=self.mensalidade/2
        
    
    def mostra(self):
        mensagem=self.matricula + '- '+self.nome
        if self.bolsista==1:
            mensagem=mensagem+"- Bolsista -"+"Mensalidade -" + str(self.mensalidade)+"$"
        else:
           mensagem=mensagem+" - Não é bolsista - "+"Mensalidade - " + str(self.mensalidade)+"$"
        return  mensagem


def btn_click():
    obj=Aluno(nome.get(),matricula.get(),var.get())
    obj.calculaM()
    lb['text']=obj.mostra()

janela=Tk()
janela.geometry("500x500")
janela.title("Cadastro de Aluno")
lb=Label(janela,text='Matrícula : ')
lb.place(x=50,y=50)
matricula=Entry(janela)
matricula.place(x=110,y=50)
lb=Label(janela,text='Nome :')
lb.place(x=50,y=70)
nome=Entry(janela)
nome.place(x=110,y=70)
lb=Label(janela,text='É Bolsista??')
lb.place(x=50,y=90)

var = IntVar()
R1 = Radiobutton(janela, text='SIM', variable=var, value=1)
R1.place(x=50,y=110)
R1 = Radiobutton(janela, text='NÃO', variable=var, value=2)
R1.place(x=50,y=130)
bt=Button(janela,text=' Criar',command=btn_click)
bt.place(x=50,y=160)
lb=Label(janela,text='')
lb.place(x=50,y=210)

janela.mainloop()