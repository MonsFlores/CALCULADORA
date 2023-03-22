from tkinter import *
from math import *
import tkinter
from tkinter import ttk
import tkinter as tk

root =Tk()
root.title("SERIE  U1")
numero= StringVar()
numerob= StringVar()
resultado= StringVar()
r=StringVar()
borrar = StringVar()

ventanaPrincipal=Frame(root, bg="#FA8072")
ventanaPrincipal.grid()

def borrar():
    numero1.set("")
    numero2.set("")
    r.set("")


def Sumar():
    r.set(float(numero1.get())+float(numero2.get()))
   
    


def MULT():
    r.set(float(numero1.get())*float(numero2.get()))
   


def RESTA():
    r.set(float(numero1.get())-float(numero2.get()))


def DIV():
    r.set(float(numero1.get())/float(numero2.get()))



numero1= IntVar()
numero2= IntVar()

titulo=Label(ventanaPrincipal, text="CALCULADORA", font=("Roboto", 20), bg="#FA8072")
titulo.grid(row=1, column=2)

numero= Label(ventanaPrincipal,bg="#FA8072", text="NUMERO A:       ")
numero.grid(row=2, column=1)

numerob= Label(ventanaPrincipal,bg="#FA8072", text="NUMERO B:       ").grid(row=3, column=1)

resultado= Label(ventanaPrincipal,bg="#FA8072", text="Resultado:       ").grid(row=4, column=1)
resultadoo = Entry(ventanaPrincipal,textvariable=r).grid(row=4, column=2)

#BotonsumaSong 
botonsumaSong =Button(ventanaPrincipal, text="SUMA", fg="#000000", bg="#F5FFFA", font=("Roboto", 7, "bold"),width=5, height=2, command=Sumar)
botonsumaSong.grid(row=7, column=1)

#BotonMULTSong 
botonmultSong =Button(ventanaPrincipal, text="MULT", fg="#000000", bg="#F5FFFA", font=("Roboto", 7, "bold"),width=5, height=2, command=MULT)
botonmultSong.grid(row=7, column=2)

#BotonCSong 
botonCSong =Button(ventanaPrincipal, text="C", fg="#000000", bg="#F5FFFA", font=("Roboto", 7, "bold"),width=5, height=2, command=borrar)
botonCSong.grid(row=7, column=3)

#BotonRESTASong 
botonsumaSong =Button(ventanaPrincipal, text="RESTA", fg="#000000", bg="#F5FFFA", font=("Roboto", 7, "bold"),width=5, height=2, command=RESTA)
botonsumaSong.grid(row=9, column=1)

#BotonDIVISIONSong 
botondivisionSong =Button(ventanaPrincipal, text="DIVISION", fg="#000000", bg="#F5FFFA", font=("Roboto", 7, "bold"),width=9, height=2,command=DIV)
botondivisionSong.grid(row=9, column=2)

#Boton=Song 
botonigualSong =Button(ventanaPrincipal, text="=", fg="#000000", bg="#F5FFFA", font=("Roboto", 7, "bold"),width=5, height=2)
botonigualSong.grid(row=9, column=3)


numero1Texto= Entry(ventanaPrincipal,textvariable=numero1).grid(row=2, column=2)
numero2Texto= Entry(ventanaPrincipal,textvariable=numero2).grid(row=3, column=2)


root.mainloop()