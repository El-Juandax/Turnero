import tkinter as tk
from datetime import datetime 
from tkinter import messagebox, ttk
import pyodbc
from tkinter.font import BOLD
import util.generic as utl
import src.Inicio.InicioDiseno as Inicio
import src.conexion.Conexion as Conexion
import os

class DisenaAsignar:
    
    def navegarR(self):
        pass
    
    def registrar(self):
        pass
    
    def salir(self):
        pass
    
    def actu_dinamica(self):
        pass
    
    def my_upper(self):
        pass
    
    def my_upper2(self):
        pass
    
    def mostrar_datos(self):
        pass
    
    def __init__(self):
        
        #Conexion para mostrar datos
        conn = Conexion.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Oficina")
        datos = cursor.fetchall()
        conn.close()
        self.oficinas = []
        
        for i in datos:
            self.oficinas.append(i[1])
        #Conexion para mostrar datos
        
        self.ventana = tk.Tk()
        self.ventana.title("Asignar Turno")
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "ICONO.ico")
        self.ventana.iconbitmap(ruta_imagen)
        self.ventana.geometry("300x350")
        self.ventana.resizable(0, 0)
        utl.centrar_ventana(self.ventana, 300, 350)
        
        #ventana formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, background="")
        frame_form.pack(fill=tk.BOTH, expand=tk.YES)
        #ventana formulario
        
        #Cabecera
        frame_form_top=tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID)
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Asignar Turno", font=('Arial narrow', 20, BOLD), fg="black", pady=20, background="WHITE")
        title.pack(expand=tk.YES, fill=tk.BOTH)
        #Cabecera
        
        #Formulario
        frame_form_fill=tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID, background="WHITE")
        frame_form_fill.pack(side="bottom", fill=tk.BOTH, expand=tk.YES)
        
        self.etiqueta1=tk.Label(frame_form_fill, text="Proveedor", font=("Arial narrow", 14, BOLD), anchor="w", background="#FCFCFC")
        self.etiqueta1.pack(fill=tk.X, padx=20, pady=5)
        self.string = tk.StringVar()
        self.entrada1=tk.Entry(frame_form_fill, textvariable=self.string, width=20, font=("Arial", 14), bg="#d2d4d2")
        self.entrada1.pack(fill=tk.X, padx=20, pady=5)
        self.string.trace("w", self.my_upper)    
        
        self.etiqueta2=tk.Label(frame_form_fill, text="Oficina", font=("Arial narrow", 14, BOLD), anchor="w", background="WHITE")
        self.etiqueta2.pack(fill=tk.X, padx=20, pady=5)
        self.string2 = tk.StringVar()
        self.entrada2=ttk.Combobox(frame_form_fill, textvariable=self.string2, width=20, font=("Arial", 14))
        self.entrada2.pack(fill=tk.X, padx=20, pady=5)
        self.entrada2.config(values=self.oficinas)
        self.entrada2.bind('<KeyRelease>', self.actu_dinamica)
        self.string2.trace("w", self.my_upper2)
        
        self.boton1=tk.Button(frame_form_fill, text="Registrar", command=self.registrar, font=("Arial", 14), bg="#08a04b", foreground="white", bd=0)
        self.boton1.pack(fill=tk.X, padx=20, pady=5)
        self.boton1.bind("<Return>", (lambda event: self.registrar()))
        
        self.boton2=tk.Button(frame_form_fill, text="Salir", command=self.salir, font=("Arial", 14), bd=0, background="#08a04b", foreground="white")
        self.boton2.pack(fill=tk.X, padx=20, pady=5)
        self.boton2.bind("<Return>", (lambda event: self.salir()))
        
        self.ventana.mainloop()
            
    