import tkinter as tk
from tkcalendar import DateEntry

def opcion1():
    etiqueta.config(text="Número de vuelo seleccionado")
    mostrar_elementos_numero_vuelo()
    ocultar_elementos_ruta_fecha()

def opcion2():
    etiqueta.config(text="Ruta y fecha seleccionada")
    mostrar_elementos_ruta_fecha()
    ocultar_elementos_numero_vuelo()

def buscar():
    # Lógica para realizar la búsqueda con los datos ingresados
    pass

def cerrar():
    reserva.destroy()

def mostrar_elementos_ruta_fecha():
    etiqueta_aeropuerto_salida.grid(row=3, column=0, pady=(0, 5))
    aeropuerto_salida_listbox.grid(row=4, column=0, pady=(0, 5))
    etiqueta_aeropuerto_destino.grid(row=5, column=0, pady=(0, 5))
    aeropuerto_destino_listbox.grid(row=6, column=0, pady=(0, 5))
    etiqueta_fecha_salida_ruta.grid(row=7, column=0, pady=(0, 5))
    fecha_salida_listbox.grid(row=8, column=0, pady=(0, 20))

def ocultar_elementos_ruta_fecha():
    etiqueta_aeropuerto_salida.grid_forget()
    aeropuerto_salida_listbox.grid_forget()
    etiqueta_aeropuerto_destino.grid_forget()
    aeropuerto_destino_listbox.grid_forget()
    etiqueta_fecha_salida_ruta.grid_forget()
    fecha_salida_listbox.grid_forget()

def mostrar_elementos_numero_vuelo():
    etiqueta_numero_vuelo.grid(row=3, column=0, pady=(0, 5))
    numero_vuelo_entry.grid(row=4, column=0, pady=(0, 5))
    etiqueta_fecha_salida.grid(row=5, column=0, pady=(0, 5))
    fecha_salida_entry.grid(row=6, column=0, pady=(0, 20))

def ocultar_elementos_numero_vuelo():
    etiqueta_numero_vuelo.grid_forget()
    numero_vuelo_entry.grid_forget()
    etiqueta_fecha_salida.grid_forget()
    fecha_salida_entry.grid_forget()

reserva = tk.Tk()
reserva.title("")
reserva.geometry("800x600")
reserva.resizable(False, False)
reserva.overrideredirect(1)

ancho_pantalla = reserva.winfo_screenwidth()
altura_pantalla = reserva.winfo_screenheight()
x = (ancho_pantalla // 2) - (800 // 2)
y = (altura_pantalla // 2) - (600 // 2)
reserva.geometry("800x600+{}+{}".format(x, y))

marco_central = tk.Frame(reserva)
marco_central.pack(expand=True)

etiqueta = tk.Label(marco_central, text="")
etiqueta.grid(row=0, column=0, pady=(100, 5))

opcion_var = tk.IntVar()
radio_numero_vuelo = tk.Radiobutton(marco_central, text="Número de vuelo", variable=opcion_var, value=1, command=opcion1)
radio_numero_vuelo.grid(row=1, column=0, pady=(0, 5))
radio_ruta_fecha = tk.Radiobutton(marco_central, text="Ruta y fecha", variable=opcion_var, value=2, command=opcion2)
radio_ruta_fecha.grid(row=2, column=0, pady=(0, 5))

etiqueta_numero_vuelo = tk.Label(marco_central, text="Número de vuelo:")
numero_vuelo_entry = tk.Entry(marco_central)

etiqueta_fecha_salida = tk.Label(marco_central, text="Fecha de salida:")
fecha_salida_entry = DateEntry(marco_central, background='darkblue', foreground='white', borderwidth=2)

aeropuertos = ["Aeropuerto 1", "Aeropuerto 2", "Aeropuerto 3"]
etiqueta_aeropuerto_salida = tk.Label(marco_central, text="Aeropuerto de salida:")
aeropuerto_salida_listbox = tk.Listbox(marco_central, selectmode=tk.SINGLE, height=3)
etiqueta_aeropuerto_destino = tk.Label(marco_central, text="Aeropuerto de destino:")
aeropuerto_destino_listbox = tk.Listbox(marco_central, selectmode=tk.SINGLE, height=3)
etiqueta_fecha_salida_ruta = tk.Label(marco_central, text="Fecha de salida:")
fecha_salida_listbox = tk.Listbox(marco_central, selectmode=tk.SINGLE, height=3)

for aeropuerto in aeropuertos:
    aeropuerto_salida_listbox.insert(tk.END, aeropuerto)
    aeropuerto_destino_listbox.insert(tk.END, aeropuerto)
    fecha_salida_listbox.insert(tk.END, aeropuerto)

boton_buscar = tk.Button(marco_central, text="Buscar", command=buscar)
boton_buscar.grid(row=9, column=0, pady=20)

boton_cerrar = tk.Button(marco_central, text="Cerrar", command=cerrar)
boton_cerrar.grid(row=10, column=0, pady=20)

marco_central.grid_columnconfigure(0, weight=1)
marco_central.grid_rowconfigure(0, weight=1)
for i in range(1, 11):
    marco_central.grid_rowconfigure(i, weight=1)

reserva.mainloop()
