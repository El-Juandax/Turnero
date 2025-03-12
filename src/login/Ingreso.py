import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from src.usuario.usuario import Usuario
from src.login.IngresoDiseno import formularioDesigner
import src.conexion.Conexion as Conexion 
from src.Inicio.Inicio import Inicio
import src.Inicio.Inicio as Inicio

class Ingreso(formularioDesigner):
    
    def salir(self):
        self.ventana_principal.destroy()
        Inicio.Inicio()
        
    def my_upper(self, *args):
        self.string.set(self.string.get().upper())
    
    def buscarUsuario(self, usuario, contrasena):
        
        conn = Conexion.conexion()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE Usuario = ? and Contrasena = ?", (usuario, contrasena))
        dato = cur.fetchone()
        cur.close()
        conn.close()
        return dato
    
    def verificar(self):
        
        usu = self.caja_texto1.get()
        pas = self.caja_texto2.get()
        
        self.buscarUsuario(usu, pas)
        if self.buscarUsuario(usu, pas) is not None:
                
            self.ventana_principal.destroy()
            Usuario(usu, pas)
            
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    
    def __init__(self):
        super().__init__()

