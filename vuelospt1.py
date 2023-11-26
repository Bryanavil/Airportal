from tkinter import ttk
from tkinter import Tk
from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

class vuelospt1:
    def __init__(self,root):
        self.root = root
        self.root.title("Selecciona vuelo")
        self.root.geometry("1540x800+0+0")
        self.root.configure(bg="white")

        ancho_pantalla = root.winfo_screenwidth()
        altura_pantalla = root.winfo_screenheight()
        x = (ancho_pantalla // 2) - (950 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
        y = (altura_pantalla // 2) - (550 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana
        root.geometry("950x550+{}+{}".format(x, y))
        

        lbltitulo=Label(self.root, bd=10, relief=RAISED, text="Selecciona tu vuelo", fg="black", bg="white")
        lbltitulo.pack(side=TOP, fill = X)


        datos=Frame(self.root, bd=20, relief=RIDGE)
        datos.place(x=0,y=50,width=940, height=400)

root=Tk()
object=vuelospt1(root)
root.mainloop()