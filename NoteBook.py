#importacion de librerias
import tkinter as tk
from tkinter import ttk, messagebox
#Crear Ventana Principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
#Crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)

#PACIENTES
#Crear Frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al NOtebook
pestañas.add(frame_pacientes, text="Pacientes")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

#DOCTORES
frame_doctores=ttk.Frame(pestañas)
#Agregar pestañas al NOtebook
pestañas.add(frame_doctores, text="Doctores")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

#NOMBRE
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)

# FECHA DE NACIMIENTO
labelFecha=tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelFecha.grid(row=1, column=0, sticky="w", padx=5, pady=5)
fechaNacimiento=tk.Entry(frame_pacientes)
fechaNacimiento.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#EDAD(readonly)
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadP=tk.Entry(frame_pacientes, state="readonly")
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#GENERO
labelGenero=tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0, sticky="w", padx=5, pady=5 )
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)

#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=4, column=1, sticky="w", padx=5, pady=5)

#TIPO DE SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)

#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_Medico=tk.StringVar()
centro_Medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_Medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", pady=5, padx=5)


ventana_principal.mainloop()
