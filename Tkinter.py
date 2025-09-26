import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Función para calcular edad
def calcular_edad(fecha_nac):
    try:
        nacimiento = datetime.strptime(fecha_nac, "%d/%m/%Y")
        hoy = datetime.today()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad
    except:
        return "Fecha inválida"

# Función para guardar datos
def guardar_datos():
    nombre = entry_nombre.get()
    fecha = entry_fecha.get()
    edad = calcular_edad(fecha)
    grupo = entry_grupo.get()
    seguro = entry_seguro.get()
    centro = entry_centro.get()
    peso = entry_peso.get()
    sexo = sexo_var.get()

    if not nombre or not fecha or not peso:
        messagebox.showwarning("Campos vacíos", "Por favor, llena todos los campos obligatorios")
        return

    with open("pacientePeso.txt", "a") as f:
        f.write(f"{nombre}|{fecha}|{edad}|{grupo}|{seguro}|{centro}|{peso}|{sexo}\n")

    messagebox.showinfo("Éxito", "Datos guardados correctamente")
    limpiar()

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_grupo.delete(0, tk.END)
    entry_seguro.delete(0, tk.END)
    entry_centro.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    sexo_var.set("")

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Pacientes")
ventana.geometry("400x400")

# Campos
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Fecha Nacimiento (dd/mm/aaaa):").pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()

tk.Label(ventana, text="Grupo Sanguíneo:").pack()
entry_grupo = tk.Entry(ventana)
entry_grupo.pack()

tk.Label(ventana, text="Tipo de Seguro:").pack()
entry_seguro = tk.Entry(ventana)
entry_seguro.pack()

tk.Label(ventana, text="Centro Médico:").pack()
entry_centro = tk.Entry(ventana)
entry_centro.pack()

tk.Label(ventana, text="Peso (kg):").pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

tk.Label(ventana, text="Sexo:").pack()
sexo_var = tk.StringVar()
tk.Radiobutton(ventana, text="Masculino", variable=sexo_var, value="M").pack()
tk.Radiobutton(ventana, text="Femenino", variable=sexo_var, value="F").pack()

tk.Button(ventana, text="Guardar", command=guardar_datos).pack()

ventana.mainloop()
