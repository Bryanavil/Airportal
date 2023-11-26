import tkinter as tk
from tkinter import messagebox

class SeleccionAsientosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleccion de Asientos")

        # Inicializar la interfaz
        self.asientos_disponibles = set(range(1, 49))
        self.asientos_seleccionados = set()
        self.crear_interfaz()

    def crear_interfaz(self):
        self.botones_asientos = []

        # Leyenda para el estatus de los asientos
        leyenda = tk.Label(self.root, text="Leyenda:\nAzul - Seleccionado\nVerde - Disponible", font=("Arial", 10))
        leyenda.grid(row=0, column=8, rowspan=8, padx=10)

        for fila in range(8):
            fila_botones = []
            for columna in range(6):
                letra_columna = chr(ord('A') + columna)
                numero_asiento = fila * 6 + columna + 1
                estado_asiento = self.obtener_estado_asiento(numero_asiento)
                boton_asiento = tk.Button(
                    self.root,
                    text=f"{letra_columna}{numero_asiento}",
                    width=5,
                    height=2,
                    command=lambda n=numero_asiento: self.toggle_asiento(n),
                    bg=estado_asiento["color"],
                    fg="white"
                )
                boton_asiento.grid(row=fila, column=columna, padx=5, pady=5)
                fila_botones.append(boton_asiento)
            self.botones_asientos.append(fila_botones)

        # Botón de confirmación
        boton_confirmar = tk.Button(self.root, text="Confirmar", command=self.confirmar_seleccion)
        boton_confirmar.grid(row=8, column=0, columnspan=6, pady=10)

        # Botón de cancelación
        boton_cancelar = tk.Button(self.root, text="Cancelar", command=self.cancelar_seleccion)
        boton_cancelar.grid(row=8, column=7, columnspan=2, pady=10)

        # Botón para volver al menú principal
        self.boton_volver = tk.Button(self.root, text="Volver al Menú", command=self.volver_al_menu)
        self.boton_volver.grid(row=8, column=9, pady=10)

    def toggle_asiento(self, numero_asiento):
        if numero_asiento in self.asientos_seleccionados:
            self.desseleccionar_asiento(numero_asiento)
        else:
            if numero_asiento in self.asientos_disponibles:
                self.seleccionar_asiento(numero_asiento)
            else:
                messagebox.showinfo("Asiento Ocupado", "Este asiento ya está ocupado.")

    def seleccionar_asiento(self, numero_asiento):
        self.asientos_seleccionados.add(numero_asiento)
        fila, columna = self.obtener_fila_columna(numero_asiento)
        self.botones_asientos[fila][columna].config(bg="blue", fg="white")
        print("Asiento seleccionado:", numero_asiento)

    def desseleccionar_asiento(self, numero_asiento):
        self.asientos_seleccionados.remove(numero_asiento)
        fila, columna = self.obtener_fila_columna(numero_asiento)
        self.botones_asientos[fila][columna].config(bg="green", fg="white")
        print("Asiento desseleccionado:", numero_asiento)

    def confirmar_seleccion(self):
        print("Asientos confirmados:", self.asientos_seleccionados)
        self.asientos_seleccionados.clear()

    def obtener_estado_asiento(self, numero_asiento):
        if numero_asiento in self.asientos_disponibles:
            return {"color": "green", "estado": "disponible"}
        elif numero_asiento in self.asientos_seleccionados:
            return {"color": "blue", "estado": "seleccionado"}
        else:
            return {"color": "", "estado": ""}

    def cancelar_seleccion(self):
        for numero_asiento in list(self.asientos_seleccionados):
            self.desseleccionar_asiento(numero_asiento)

    def obtener_fila_columna(self, numero_asiento):
        fila = (numero_asiento - 1) // 6
        columna = (numero_asiento - 1) % 6
        return fila, columna
    
    def volver_al_menu(self):
        # Puedes realizar acciones adicionales aquí antes de volver al menú
        self.root.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    app = SeleccionAsientosApp(root)
    root.mainloop()
