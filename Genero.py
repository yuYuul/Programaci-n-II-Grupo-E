
import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Selector de Edad")
# Etiqueta
labelEdad = tk.Label(ventana, text="Edad")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
# Spinbox de 1 a 10
spin = tk.Spinbox(ventana, from_=1, to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
# Función para mostrar la edad seleccionada
def mostrarEdad():
    edad = spin.get()
    messagebox.showinfo("Edad", f"La edad seleccionada es: {edad}")
# Botón para obtener el valor
boton = tk.Button(ventana, text="Obtener Valor", command=mostrarEdad)
boton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
ventana.mainloop()

labelGenero = tk.Label(ventana, text="Género")
labelGenero.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Spinbox de texto para género
genero = tk.Spinbox(ventana, values=("Masculino", "Femenino", "Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)

# Función para mostrar el género seleccionado
def mostrarGenero():
    seleccionado = genero.get()
    messagebox.showinfo("Género seleccionado", f"Has seleccionado: {seleccionado}")

# Botón para obtener género
botonGenero = tk.Button(ventana, text="Obtener género", command=mostrarGenero)
botonGenero.grid(row=3, column=0, padx=10, pady=10)

ventana.mainloop()
