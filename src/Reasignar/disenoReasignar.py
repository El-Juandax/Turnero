import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import calendar
import util.generic as utl
from tkinter.font import BOLD
import src.conexion.Conexion as Conexion
import os

class DisenoReasignar:
    
    def reasignar(self):
        pass
    
    def salir(self):
        pass
    
    def actu_dinamica(self):
        pass
    
    def my_upper(self):
        pass
    
    def my_upper2(self):
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
        self.ventana.geometry("300x400")
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "ICONO.ico")
        self.ventana.iconbitmap(ruta_imagen)
        self.ventana.resizable(0, 0)
        utl.centrar_ventana(self.ventana, 300, 400)
        
        #ventana formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, background="")
        frame_form.pack(fill=tk.BOTH, expand=tk.YES)
        #ventana formulario
        
        #Cabecera
        frame_form_top=tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID)
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Reasignar Turno", font=('Arial', 20, BOLD), fg="black", pady=20, background="#a8e4ae")
        title.pack(expand=tk.YES, fill=tk.BOTH)
        #Cabecera
        
        #Formulario
        frame_form_fill=tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID, background="#a8e4ae")
        frame_form_fill.pack(side="bottom", fill=tk.BOTH, expand=tk.YES)
        
        self.etiqueta1=tk.Label(frame_form_fill, text="Numero Turno", font=("Arial", 14), anchor="w", background="#a8e4ae")
        self.etiqueta1.pack(fill=tk.X, padx=20, pady=5)
        self.string = tk.StringVar()
        self.entrada1=tk.Entry(frame_form_fill, textvariable=self.string, width=20, font=("Arial", 14))
        self.entrada1.pack(fill=tk.X, padx=20, pady=5)
        self.string.trace("w", self.my_upper)
        
        self.etiqueta3=tk.Label(frame_form_fill, text="Fecha", font=("Arial", 14), anchor="w", background="#a8e4ae")
        self.etiqueta3.pack(fill=tk.X, padx=20, pady=5)
        self.entrada3=DateEntry(frame_form_fill, width=20, font=("Arial", 14), locale='es_ES', date_pattern='yyyy/mm/dd')
        self.entrada3.pack(fill=tk.X, padx=20, pady=5)
                
        self.etiqueta2=tk.Label(frame_form_fill, text="Oficina reasignada", font=("Arial", 14), anchor="w", background="#a8e4ae")
        self.etiqueta2.pack(fill=tk.X, padx=20, pady=5)
        self.string2 = tk.StringVar()
        self.entrada2=ttk.Combobox(frame_form_fill, textvariable=self.string2, width=20, font=("Arial", 14))
        self.entrada2.pack(fill=tk.X, padx=20, pady=5)
        self.entrada2.config(values=self.oficinas)
        self.entrada2.bind("<KeyRelease>", self.actu_dinamica)
        self.string2.trace("w", self.my_upper2)
        
        
        self.boton1=tk.Button(frame_form_fill, text="Reasignar", command=self.reasignar, font=("Arial", 14), bg="#579053", foreground="white", bd=0)
        self.boton1.pack(fill=tk.X, padx=20, pady=5)
        self.boton1.bind("<Return>", (lambda event: self.reasignar()))
        
        self.boton2=tk.Button(frame_form_fill, text="Salir", command=self.salir, font=("Arial", 14), bg="#a8e4ae", foreground="black", bd=0)
        self.boton2.pack(fill=tk.X, padx=20, pady=5)
        self.boton2.bind("<Return>", (lambda event: self.salir()))
        