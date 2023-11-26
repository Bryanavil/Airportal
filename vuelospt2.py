import tkinter as tk
from tkinter import ttk

class VentanaVuelos:
    def __init__(self, root):
        self.root = root
        self.root.title("Vuelos")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        ancho_pantalla = self.root.winfo_screenwidth()
        altura_pantalla = self.root.winfo_screenheight()
        x = (ancho_pantalla // 2) - (950 // 2)
        y = (altura_pantalla // 2) - (550 // 2)
        self.root.geometry("950x550+{}+{}".format(x, y))

        # Crear un marco para organizar los botones en la parte superior
        self.marco_botones = tk.Frame(self.root, background="white")
        self.marco_botones.pack(side=tk.TOP, fill=tk.X)


        # Agregar una barra deslizante horizontal
        self.scrollbar = ttk.Scrollbar(self.root, orient="horizontal")
        self.scrollbar.pack(side="bottom", fill="x")

        # Crear un lienzo para contener los cuadros
        self.canvas = tk.Canvas(self.root, xscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.configure(bg="white")

        # Configurar la barra deslizante para que se mueva con el lienzo
        self.scrollbar.config(command=self.canvas.xview)

        # Crear un frame interior para contener los widgets
        self.frame_interior = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_interior, anchor="nw")
        self.canvas.configure(bg="white")

        # Agregar información de vuelos
        vuelos_info = [
            {"vuelo": "Vuelo 001", "precio": "$200", "fecha": "2023-12-01"},
            {"vuelo": "Vuelo 002", "precio": "$150", "fecha": "2023-12-05"},
            {"vuelo": "Vuelo 003", "precio": "$300", "fecha": "2023-12-10"},
            {"vuelo": "Vuelo 004", "precio": "$500", "fecha": "2023-12-12"},
            {"vuelo": "Vuelo 005", "precio": "$320", "fecha": "2023-12-10"},
            {"vuelo": "Vuelo 006", "precio": "$410", "fecha": "2023-12-01"},
            # Agrega más información de vuelos según sea necesario
        ]

        # Crear cuadros con información de vuelos
        for vuelo_info in vuelos_info:
            cuadro_vuelo = tk.Frame(self.frame_interior, bd=2, relief="groove")
            cuadro_vuelo.pack(pady=5, padx=15, side="left", fill="y")

            # Mostrar información en etiquetas dentro del cuadro
            vuelo_label = tk.Label(cuadro_vuelo, text=f"Vuelo: {vuelo_info['vuelo']}")
            vuelo_label.pack(anchor="w")


            tk.Label(cuadro_vuelo, text=f"Precio: {vuelo_info['precio']}").pack(anchor="w")
            tk.Label(cuadro_vuelo, text=f"Fecha: {vuelo_info['fecha']}").pack(anchor="w")

            # Configurar el evento de clic para mostrar la información del vuelo
            vuelo_label.bind("<Button-1>", lambda event, info=vuelo_info: self.mostrar_informacion_vuelo(info))
             # Botón para volver al menú principal
        self.boton_volver = tk.Button(self.root, text="Volver al Menú", command=self.volver_al_menu)
        self.boton_volver.pack(side=tk.BOTTOM, pady=10)

        # Etiqueta para mostrar la información del vuelo seleccionado
        self.info_label = tk.Label(self.root, text="Selecciona vuelo", bg="white", pady=0)
        self.info_label.pack(side=tk.BOTTOM, fill=tk.X)


        # Configurar el lienzo para que se expanda con el contenido
        self.frame_interior.update_idletasks()
        self.frame_interior.configure(bg="white")
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


    def mostrar_informacion_vuelo(self, vuelo_info):
        # Actualizar la etiqueta con la información del vuelo seleccionado
        info_text = f"Vuelo seleccionado:\n{vuelo_info['vuelo']}\nPrecio: {vuelo_info['precio']}\nFecha: {vuelo_info['fecha']}"
        self.info_label.config(text=info_text)
    def volver_al_menu(self):
        # Puedes realizar acciones adicionales aquí antes de volver al menú
        self.root.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVuelos(root)
    root.mainloop()
