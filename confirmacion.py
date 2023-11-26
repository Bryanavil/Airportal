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
        

        lbltitulo=Label(self.root, bd=10, relief=RAISED, text="CONFIRMACION DE VUELO", fg="black")
        lbltitulo.pack(side=TOP, fill = X)


        datos=Frame(self.root, bd=20, relief=RIDGE)
        datos.place(x=0,y=50,width=950, height=500)

        datosarriba=LabelFrame(datos, bd=10, relief=RIDGE, padx=10,
                                 font=("times new roman", 25, "bold"), text="RESERVACION")
        datosarriba.place(x=5, y=5, width=900, height=250)

        datosabajo=LabelFrame(datos, bd=10, relief=RIDGE, padx=10,
                                 font=("times new roman", 25, "bold"), text="INFORMACION VUELO")
        datosabajo.place(x=5, y=280, width=900, height=175)

        #datos arriba

        lblreser=Label(datosarriba, text="Clave de reservacion", font=("times new roman", 19,"bold"), padx=10,pady=6)
        lblreser.grid(row=0,column=0, sticky=W)
        txtref=Label(datosarriba,text="662597", font=("times new roman", 19,"bold"), width=15)
        txtref.grid(row=0, column=1)

        lblfecha=Label(datosarriba, text="Fecha de reservacion", font=("times new roman", 19,"bold"), padx=10,pady=6)
        lblfecha.grid(row=2,column=0, sticky=W)
        txtreffecha=Label(datosarriba, text="0/0/0",font=("times new roman", 19,"bold"), width=15)
        txtreffecha.grid(row=2, column=1)

        lbltitular=Label(datosarriba, text="Titular de reservacion", font=("times new roman", 19,"bold"), padx=10,pady=6)
        lbltitular.grid(row=4,column=0, sticky=W)
        txtreftit=Label(datosarriba, text="samanta",font=("times new roman", 19,"bold"), width=15)
        txtreftit.grid(row=4, column=1)


        #datos abajo

        ciudad_salida_label = Label(datosabajo, text="Ciudad de Salida:", font=("times new roman", 10, "bold"))
        ciudad_salida_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        ciudad_salida_valor = Label(datosabajo, text="Ciudad 1", font=("times new roman", 10))
        ciudad_salida_valor.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Fecha de salida
        fecha_salida_label = Label(datosabajo, text="Fecha de Salida:", font=("times new roman", 10, "bold"))
        fecha_salida_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        fecha_salida_valor = Label(datosabajo, text="Fecha 1", font=("times new roman", 10))
        fecha_salida_valor.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Barra separadora
        barra_separadora = Canvas(datosabajo, height=2, bg="black")
        barra_separadora.grid(row=0, column=100, pady=10, sticky="we")
        
        # Ciudad de llegada
        ciudad_llegada_label = Label(datosabajo, text="Ciudad de Llegada:", font=("times new roman", 10, "bold"))
        ciudad_llegada_label.grid(row=0, column=120, padx=10, pady=5, sticky="w")
        
        ciudad_llegada_valor = Label(datosabajo, text="Ciudad 2", font=("times new roman", 10))
        ciudad_llegada_valor.grid(row=0, column=121, padx=10, pady=5, sticky="w")

        # Fecha de salida
        fecha_entrada_label = Label(datosabajo, text="Fecha de llegada:", font=("times new roman", 10, "bold"))
        fecha_entrada_label.grid(row=1, column=120, padx=10, pady=5, sticky="w")
        
        fecha_entrada_valor = Label(datosabajo, text="Fecha 1", font=("times new roman", 10))
        fecha_entrada_valor.grid(row=1, column=121, padx=10, pady=5, sticky="w")
        
        # Fecha de abordaje
        fecha_abordaje_label = Label(datosabajo, text="Fecha de Abordaje:", font=("times new roman", 10, "bold"))
        fecha_abordaje_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        fecha_abordaje_valor = Label(datosabajo, text="Fecha 2", font=("times new roman", 10))
        fecha_abordaje_valor.grid(row=3, column=1, padx=10, pady=20, sticky="w")


root=Tk()
object=vuelospt1(root)
root.mainloop()