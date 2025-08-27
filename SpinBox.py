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
