import tkinter as tk
from tkinter import ttk, messagebox
from src.usuario.disenoUsuario import DisenoUsuario
import src.conexion.Conexion as Conexion 
from src.Inicio.Inicio import Inicio
import src.Inicio.Inicio as Inicio
from datetime import datetime

class Usuario(DisenoUsuario):
    
    def __init__(self, usuario, contrasena):       
        self.usuario = usuario
        self.contrasena = contrasena
        self.turno_detenido = False  # Bandera para rastrear si el turno ha sido detenido
        super().__init__()

    
    def salir(self):
        pregunta = messagebox.askquestion("Salir", "¿Esta seguro que desea salir?")
        if pregunta == "yes":
            self.ventana.after_cancel(self.actu)
            self.ventana.after_cancel(self.sele)
            self.ventana.destroy()
            Inicio.Inicio()
        else:
            pass
    
    def seleccion_tabla(self):
        try:
            self.tabla.delete(*self.tabla.get_children())
            
            conn = Conexion.conexion()
            now = datetime.now()
            fecha = now.strftime("%Y-%m-%d")
            print(fecha)
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE Usuario = ? AND Contrasena = ?",(self.usuario, self.contrasena))
            id = cursor.fetchone()
            cursor.execute("SELECT Numero_Turno, Proveedor FROM turnos WHERE Id_Usuario = ? and Estado = 'ACTIVO'", (id))
            datos = cursor.fetchall()
            
            print(datos)
            
            if datos is None:
                
                self.tabla.insert("", "end", values=("No hay turnos asignados", "No hay proveedores"))
                
            else:
                
                datos_agregados = set()
                
                for dato in datos:
                    datos_str=tuple(dato)
                    if datos_str not in datos_agregados:
                        self.tabla.insert("", "end", values=(dato[0], dato[1])) 
                        datos_agregados.add(datos_str)
                        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar a la base de datos {e}",)
        
        finally:
            
            cursor.close()
            conn.close()
            self.sele = self.ventana.after(30000, self.seleccion_tabla)    
            
    def mostrar_datos(self):
        
        conn = Conexion.conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT Nombre FROM usuarios WHERE Usuario = ? AND Contrasena = ?", (self.usuario, self.contrasena))
        datos = cursor.fetchone()
        conn.close()
        
        self.label.config(text=f"Bienvenido, {datos[0]}")
        
    def Turnos(self):
        
        conn = Conexion.conexion()
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("Select id from Usuarios where Usuario = ? and Contrasena = ?", (self.usuario, self.contrasena))
        id = cursor.fetchone()
        print(id)
        cursor1.execute("select T.id, Numero_Turno, Proveedor from Turnos as T inner join Usuarios as U on U.id=T.Id_Usuario where T.Id_Usuario=? and Estado='ACTIVO' or T.Id_Usuario=? and Estado='ATENDIENDO'", (id[0], id[0]))
        datos = cursor1.fetchone()
        print(datos)
        conn.close()
        
        if datos == None:
            self.Codigo.config(text=f"No hay turnos asignados")
            self.Proveedor.config(text=f"No hay turnos asignados")
        else:
            conn = Conexion.conexion()
            update = conn.cursor()
            self.id.config(text=f"{datos[0]}")
            self.Codigo.config(text=f"{datos[1]}")
            self.Proveedor.config(text=f"{datos[2]}")
            update.execute("Update Turnos set Estado='ATENDIENDO' where id=? and Id_Usuario=?",(datos[0], id[0]))
            update.commit()
            update.close()
            conn.close()
            
        self.actu=self.ventana.after(30000, self.Turnos)    
        
    def detener(self):
        
        self.actualizar_turnos = False
        numero_turno = self.id.cget("text")
        pregunta = messagebox.askquestion("Terminar Turno", "¿Desea terminar el turno?")
        if pregunta == "yes":
            conn = Conexion.conexion()
            cursor = conn.cursor()
            cursor.execute("UPDATE Turnos SET Estado='TERMINADO' WHERE ID = ?", numero_turno)
            conn.commit()
            conn.close()
            self.Codigo.config(background="red")
            self.Proveedor.config(background="red")
            self.ventana.after_cancel(self.actu)
            messagebox.showinfo("Turnos", "Turno terminado")
            self.turno_detenido = True  # Actualizar la bandera a True
        else:
            pass

    def siguienteT(self):
        if not self.turno_detenido:
            messagebox.showwarning("Turnos", "Debe terminar el turno actual antes de pasar al siguiente.")
            return
        
        numero_turno = self.Codigo.cget("text")
        
        if numero_turno == "No hay turnos asignados":
            messagebox.showinfo("Turnos", "No hay turnos asignados")
        else:
            pregunta = messagebox.askquestion("Siguiente Turno", "¿Desea pasar al siguiente turno?")
            if pregunta == "yes":
                self.Codigo.config(background="white")
                self.Proveedor.config(background="white")
                self.Turnos()
                self.turno_detenido = False  # Restablecer la bandera a False
            else:
                pass