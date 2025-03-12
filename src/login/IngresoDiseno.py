import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from src.Inicio.Inicio import Inicio
import src.Inicio.Inicio as Inicio
import os

class formularioDesigner:
    
    def verificar(self):
        pass
    
    def salir(self):
        pass
    
    def my_upper(self):
        pass  
    
    def my_upper2(self):
        pass
    
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Ingreso")
        self.ventana_principal.geometry("300x400")
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "ICONO.ico")
        self.ventana_principal.iconbitmap(ruta_imagen)
        self.ventana_principal.resizable(0, 0)
        utl.centrar_ventana(self.ventana_principal, 300, 400)
        
        #ventana formulario
        frame_form = tk.Frame(self.ventana_principal, bd= 0, relief=tk.SOLID)
        frame_form.pack( fill=tk.BOTH, expand=tk.YES)
        #ventana formulario
        
        #Frame_form_top
        frame_form_top = tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID)
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de Sesión", font=('Arial narrow', 20, BOLD), fg="black", background="WHITE", pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        #frame_form_top
        
        #Frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=30, bd=0, background="WHITE", relief=tk.SOLID)
        frame_form_fill.pack(side="bottom", fill=tk.BOTH, expand=tk.YES)
        
        self.etiqueta1 = tk.Label(frame_form_fill, text="Escribe tu nombre de usuario", background="WHITE", font=("arial narrow", 14, BOLD), anchor="w")
        self.etiqueta1.pack(fill=tk.X, padx=20, pady=5)
        self.string = tk.StringVar()       
        self.caja_texto1 =tk.Entry(frame_form_fill, textvariable=self.string, font=("arial", 14,), bg="#d2d4d2")
        self.caja_texto1.pack(fill=tk.X, padx=20, pady=10) 
        self.string.trace("w", self.my_upper)
        
        self.etiqueta2 = tk.Label(frame_form_fill, text="Escribe tu contraseña", background="WHITE", font=("arial narrow", 14, BOLD), anchor="w")
        self.etiqueta2.pack(fill=tk.X, padx=20, pady=5) 
        self.caja_texto2 =tk.Entry(frame_form_fill, width=20, font=("arial", 14), show="*", bg="#d2d4d2")
        self.caja_texto2.pack(fill=tk.X, padx=20, pady=10)  

        boton1 = tk.Button(frame_form_fill, text="Iniciar", font=("arial", 14, ), command=self.verificar, foreground="WHITE", bd=0, background="#08a04b")
        boton1.pack(fill=tk.X, padx=20, pady=20) 
        boton1.bind("<Return>", (lambda event: self.verificar()))
        
        boton1 = tk.Button(frame_form_fill, text="Salir", font=("arial", 14, ), foreground="white", command=self.salir, bd=0, background="#08a04b")
        boton1.pack(fill=tk.X, padx=20, pady=0) 
        boton1.bind("<Return>", (lambda event: self.salir()))
        
        self.ventana_principal.mainloop()