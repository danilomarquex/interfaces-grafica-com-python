#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Nov 23, 2021 01:18:32 AM -03  platform: Windows NT
from tkinter import *
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class Toplevel1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'


        self.root = tk.Tk()
        self.root.geometry("600x450+333+117")
        self.root.minsize(120, 1)
        self.root.maxsize(1370, 749)
        self.root.resizable(1,  1)
        self.root.title("Login")
        self.root.configure(background="#050A30")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")

        self.frameCadastro = tk.Frame(self.root)
        self.frameCadastro.place(relx=0.1, rely=0.067, relheight=0.833, relwidth=0.825)
        self.frameCadastro.configure(relief='groove')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(relief="groove")
        self.frameCadastro.configure(background="#000c66")
        self.frameCadastro.configure(highlightbackground="#d9d9d9")
        self.frameCadastro.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.frameCadastro)
        self.Entry1.place(relx=0.115, rely=0.339, height=30, relwidth=0.695)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(self.frameCadastro, show = '*')
        self.Entry2.place(relx=0.115, rely=0.563, height=30, relwidth=0.695)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Label1Cadastro = tk.Label(self.frameCadastro)
        self.Label1Cadastro.place(relx=0.368, rely=0.056, height=43, width=130)
        self.Label1Cadastro.configure(activebackground="#000C66")
        self.Label1Cadastro.configure(activeforeground="white")
        self.Label1Cadastro.configure(activeforeground="black")
        self.Label1Cadastro.configure(background="#000C66")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {SimSun} -size 16 -weight bold")
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro.configure(highlightcolor="black")
        self.Label1Cadastro.configure(text='''Login''')

        self.Button1Cadastro = tk.Button(self.frameCadastro, command = self.LoginBackEnd)
        self.Button1Cadastro.place(relx=0.368, rely=0.677, height=44, width=107)
        self.Button1Cadastro.configure(activebackground="#ececec")
        self.Button1Cadastro.configure(activeforeground="#000000")
        self.Button1Cadastro.configure(background="#0000FF")
        self.Button1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro.configure(font="-family {SimSun} -size 15")
        self.Button1Cadastro.configure(foreground="#ffffff")
        self.Button1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro.configure(highlightcolor="black")
        self.Button1Cadastro.configure(pady="0")
        self.Button1Cadastro.configure(text='''Logar''')

        self.Button1Cadastro_1 = tk.Button(self.frameCadastro, command = self.Cadastro)
        self.Button1Cadastro_1.place(relx=0.368, rely=0.816, height=44, width=107)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#0000FF")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(font="-family {SimSun} -size 15")
        self.Button1Cadastro_1.configure(foreground="#ffffff")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''Cadastrar''')

        self.Label1Cadastro_1 = tk.Label(self.frameCadastro)
        self.Label1Cadastro_1.place(relx=0.069, rely=0.451, height=33, width=130)
        self.Label1Cadastro_1.configure(activebackground="#000C66")
        self.Label1Cadastro_1.configure(activeforeground="white")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#000C66")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {SimSun} -size 16 -weight bold")
        self.Label1Cadastro_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Senha:''')

        self.Label1Cadastro_1_1 = tk.Label(self.frameCadastro)
        self.Label1Cadastro_1_1.place(relx=0.093, rely=0.224, height=33, width=129)
        self.Label1Cadastro_1_1.configure(activebackground="#000C66")
        self.Label1Cadastro_1_1.configure(activeforeground="white")
        self.Label1Cadastro_1_1.configure(activeforeground="black")
        self.Label1Cadastro_1_1.configure(background="#000C66")
        self.Label1Cadastro_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1_1.configure(font="-family {SimSun} -size 16 -weight bold")
        self.Label1Cadastro_1_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1_1.configure(highlightcolor="black")
        self.Label1Cadastro_1_1.configure(text='''Usuário:''')
        self.root.mainloop() 
    

    def Cadastro(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'


        self.cadastro = tk.Tk()
        self.cadastro.geometry("600x450+333+117")
        self.cadastro.minsize(120, 1)
        self.cadastro.maxsize(1370, 749)
        self.cadastro.resizable(1,  1)
        self.cadastro.title("Cadastro")
        self.cadastro.configure(background="#050A30")
        self.cadastro.configure(highlightbackground="#d9d9d9")
        self.cadastro.configure(highlightcolor="black")

        self.frameCadastro = tk.Frame(self.cadastro)
        self.frameCadastro.place(relx=0.1, rely=0.067, relheight=0.833, relwidth=0.825)
        self.frameCadastro.configure(relief='groove')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(relief="groove")
        self.frameCadastro.configure(background="#000c66")
        self.frameCadastro.configure(highlightbackground="#d9d9d9")
        self.frameCadastro.configure(highlightcolor="black")

        self.Entry1Cadastro = tk.Entry(self.frameCadastro)
        self.Entry1Cadastro.place(relx=0.115, rely=0.339, height=30, relwidth=0.695)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Entry1Cadastro.configure(highlightcolor="black")
        self.Entry1Cadastro.configure(insertbackground="black")
        self.Entry1Cadastro.configure(selectbackground="blue")
        self.Entry1Cadastro.configure(selectforeground="white")

        self.Entry2Cadastro = tk.Entry(self.frameCadastro, show = '*')
        self.Entry2Cadastro.place(relx=0.115, rely=0.563, height=30, relwidth=0.695)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(highlightbackground="#d9d9d9")
        self.Entry2Cadastro.configure(highlightcolor="black")
        self.Entry2Cadastro.configure(insertbackground="black")
        self.Entry2Cadastro.configure(selectbackground="blue")
        self.Entry2Cadastro.configure(selectforeground="white")

        self.Label1Cadastro = tk.Label(self.frameCadastro)
        self.Label1Cadastro.place(relx=0.368, rely=0.056, height=43, width=130)
        self.Label1Cadastro.configure(activebackground="#000C66")
        self.Label1Cadastro.configure(activeforeground="white")
        self.Label1Cadastro.configure(activeforeground="black")
        self.Label1Cadastro.configure(background="#000C66")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {SimSun} -size 16 -weight bold")
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro.configure(highlightcolor="black")
        self.Label1Cadastro.configure(text='''Cadastro''')

        self.Button1Cadastro_1 = tk.Button(self.frameCadastro, command = self.CadastarBackEnd)
        self.Button1Cadastro_1.place(relx=0.368, rely=0.816, height=44, width=107)
        self.Button1Cadastro_1.configure(activebackground="#ececec")
        self.Button1Cadastro_1.configure(activeforeground="#000000")
        self.Button1Cadastro_1.configure(background="#0000FF")
        self.Button1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro_1.configure(font="-family {SimSun} -size 15")
        self.Button1Cadastro_1.configure(foreground="#ffffff")
        self.Button1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro_1.configure(highlightcolor="black")
        self.Button1Cadastro_1.configure(pady="0")
        self.Button1Cadastro_1.configure(text='''Cadastrar''')

        self.Label1Cadastro_1 = tk.Label(self.frameCadastro)
        self.Label1Cadastro_1.place(relx=0.069, rely=0.451, height=33, width=130)
        self.Label1Cadastro_1.configure(activebackground="#000C66")
        self.Label1Cadastro_1.configure(activeforeground="white")
        self.Label1Cadastro_1.configure(activeforeground="black")
        self.Label1Cadastro_1.configure(background="#000C66")
        self.Label1Cadastro_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1.configure(font="-family {SimSun} -size 16 -weight bold")
        self.Label1Cadastro_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1.configure(highlightcolor="black")
        self.Label1Cadastro_1.configure(text='''Senha:''')

        self.Label1Cadastro_1_1 = tk.Label(self.frameCadastro)
        self.Label1Cadastro_1_1.place(relx=0.093, rely=0.224, height=33, width=129)
        self.Label1Cadastro_1_1.configure(activebackground="#000C66")
        self.Label1Cadastro_1_1.configure(activeforeground="white")
        self.Label1Cadastro_1_1.configure(activeforeground="black")
        self.Label1Cadastro_1_1.configure(background="#000C66")
        self.Label1Cadastro_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro_1_1.configure(font="-family {SimSun} -size 16 -weight bold")
        self.Label1Cadastro_1_1.configure(foreground="#ffffff")
        self.Label1Cadastro_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1Cadastro_1_1.configure(highlightcolor="black")
        self.Label1Cadastro_1_1.configure(text='''Usuário:''')
        self.root.mainloop()
        
    def CadastarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get() + '\n')

            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry2Cadastro.get() + '\n')
            self.cadastro.destroy()
        except:
            print('Houve um erro!')

    def LoginBackEnd(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()
        
        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))
        senhas = list(map(lambda x: x.replace('\n', ''), senhas))
        
        usuario = self.Entry1.get()
        senha = self.Entry2.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print('Usuario logado')
                logado = True
                self.root.destroy()
                break
        if not logado:
            print('Usuario ou senha incorretos')
            self.root.destroy()
        


Toplevel1()



