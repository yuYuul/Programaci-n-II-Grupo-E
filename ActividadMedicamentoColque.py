import tkinter as tk
from tkinter import ttk, messagebox
import os
 
ARCHIVO = "medicamento.txt"
 
# ----------------------------
# Función para dar formato a la fecha (dd-mm-yyyy)
# ----------------------------
def formatear_fecha(event=None):
    s = var_fecha.get()
    digitos = ''.join(c for c in s if c.isdigit())[:8]
 
    if len(digitos) > 4:
        nuevo = f"{digitos[:2]}-{digitos[2:4]}-{digitos[4:]}"
    elif len(digitos) > 2:
        nuevo = f"{digitos[:2]}-{digitos[2:]}"
    else:
        nuevo = digitos
 
    if nuevo != s:
        var_fecha.set(nuevo)
        entry_fecha.icursor(tk.END)
 
# ----------------------------
# Guardar registro
# ----------------------------
def registrar():
    nombre = entry_nombre.get().strip()
    presentacion = combo_present.get().strip()
    dosis = entry_dosis.get().strip()
    fecha = var_fecha.get().strip()
 
    if not nombre or not presentacion or not dosis or not fecha:
        messagebox.showwarning("Campos vacíos", "Complete todos los campos antes de registrar.")
        return
 
    # Guardar en archivo
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre}|{presentacion}|{dosis}|{fecha}\n")
 
    # Mostrar en Treeview
    tree.insert("", tk.END, values=(nombre, presentacion, dosis, fecha))
 
    # Limpiar campos
    entry_nombre.delete(0, tk.END)
    combo_present.set("")
    entry_dosis.delete(0, tk.END)
    var_fecha.set("")
 
# ----------------------------
# Cargar registros
# ----------------------------
def cargar_registros():
    if not os.path.exists(ARCHIVO):
        return
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split("|")
            if len(datos) == 4:
                tree.insert("", tk.END, values=tuple(datos))
 
# ----------------------------
# Eliminar registro
# ----------------------------
def eliminar():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning("Sin selección", "Seleccione un registro para eliminar.")
        return
 
    valores = tree.item(seleccion, "values")
 
    # Eliminar del Treeview
    tree.delete(seleccion)
 
    # Reescribir archivo excluyendo el eliminado
    registros = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip().split("|") != list(valores):
                registros.append(linea)
 
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.writelines(registros)
 
    messagebox.showinfo("Eliminado", "Registro eliminado con éxito.")
 
# ----------------------------
# Interfaz gráfica
# ----------------------------
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("750x480")
ventana.minsize(650, 400)
 
# Marco de formulario
frm_form = ttk.Frame(ventana, padding=10)
frm_form.pack(fill="x")
 
ttk.Label(frm_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nombre = ttk.Entry(frm_form)
entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
 
ttk.Label(frm_form, text="Presentación:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
combo_present = ttk.Combobox(frm_form, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
combo_present.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
 
ttk.Label(frm_form, text="Dosis:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_dosis = ttk.Entry(frm_form)
entry_dosis.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
 
ttk.Label(frm_form, text="Fecha Vencimiento:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
var_fecha = tk.StringVar()
entry_fecha = ttk.Entry(frm_form, textvariable=var_fecha)
entry_fecha.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
entry_fecha.bind("<KeyRelease>", formatear_fecha)
 
frm_form.columnconfigure(1, weight=1)
 
# Botones
frm_btn = ttk.Frame(ventana)
frm_btn.pack(fill="x", pady=8)
 
btn_registrar = ttk.Button(frm_btn, text="Registrar", command=registrar)
btn_registrar.pack(side="left", expand=True, padx=10)
 
btn_eliminar = ttk.Button(frm_btn, text="Eliminar", command=eliminar)
btn_eliminar.pack(side="left", expand=True, padx=10)
 
# Lista de registros
frm_lista = ttk.Frame(ventana, padding=10)
frm_lista.pack(fill="both", expand=True)
 
tree = ttk.Treeview(frm_lista, columns=("nombre", "presentacion", "dosis", "fecha"), show="headings")
tree.heading("nombre", text="Nombre")
tree.heading("presentacion", text="Presentación")
tree.heading("dosis", text="Dosis")
tree.heading("fecha", text="Fecha Vencimiento")
 
tree.column("nombre", width=220)
tree.column("presentacion", width=120, anchor="center")
tree.column("dosis", width=100, anchor="center")
tree.column("fecha", width=120, anchor="center")
 
tree.grid(row=0, column=0, sticky="nsew")
 
scroll = ttk.Scrollbar(frm_lista, orient="vertical", command=tree.yview)
scroll.grid(row=0, column=1, sticky="ns")
tree.configure(yscrollcommand=scroll.set)
 
frm_lista.rowconfigure(0, weight=1)
frm_lista.columnconfigure(0, weight=1)
 
cargar_registros()
 
ventana.mainloop()
 