from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from datetime import datetime
import src.conexion.Conexion as Conexion
import pyodbc
from src.Asignar.DisenaAsignarT import DisenaAsignar
from src.Reasignar.reasignarTurnos import Reasignar
import src.Inicio.Inicio as inicio

class Asignar(DisenaAsignar):

    def navegarR(self):
        self.ventana.destroy()
        Reasignar()

    def my_upper(self, *args):
        self.string.set(self.string.get().upper())

    def my_upper2(self, *args):
        self.string2.set(self.string2.get().upper())

    def actu_dinamica(self, event):
        self.texto_ingresado = self.entrada2.get()
        self.opciones_filtradas = [opcion for opcion in self.oficinas if self.texto_ingresado in opcion]
        self.entrada2['values'] = self.opciones_filtradas

    def salir(self):
        self.ventana.destroy()
        inicio.Inicio()

    def registrar(self):
        try:
            
            conn = Conexion.conexion()
            
            if conn is not None:
                
                cursor = conn.cursor()
                estado = "ACTIVO"
                now = datetime.now()
                fecha = now.strftime("%Y-%m-%d")
                oficina = self.entrada2.get()
                proveedor = self.entrada1.get()

                if not oficina or not proveedor:
                    messagebox.showerror("Error", "Por favor, complete todos los campos.")
                    return

                cursor.execute("SELECT Id FROM oficina WHERE Nombre = ?", (oficina,))
                id_oficina = cursor.fetchone()
                
                cursor.execute("SELECT id FROM Usuarios WHERE Id_oficina = ?", (id_oficina[0],))
                id_usuario = cursor.fetchone()
                
                cursor.execute("SELECT MAX(Numero_Turno), MAX(Fecha) FROM Turnos WHERE Id_Usuario = ? and fecha = ?", (id_usuario[0], fecha))
                numero_turno = cursor.fetchone()
                
                cursor.execute("SELECT Inicial from Oficina WHERE Nombre = ?", (oficina))
                inicial = cursor.fetchone()
                print(numero_turno[0])# Obtener el valor de la tupla
            
                if numero_turno[0] is None and numero_turno[1] is None:
                    
                    numero_turno = 1  # La tabla está vacía, el primer turno es 1
                    turno = str(inicial[0]) + str(numero_turno) 
                    
                else:
                    
                    ultimo_turno = numero_turno[0]
                    print(ultimo_turno)
                    ultima_fecha = numero_turno[1]
                    
                    if ultima_fecha != fecha:
                    
                        numero_turno = 1
                        turno = str(inicial[0]) + str(numero_turno) 
                              
                    else:
                    
                        numero_turno = 1 + int(ultimo_turno.replace(f"{inicial[0]}", "")) 
                        print(numero_turno) 
                        turno = str(inicial[0]) + str(numero_turno)   
                              
                
                ID = str(id_usuario[0]) + str(turno) + str(fecha.replace("-", "")) 
                
                if not id_oficina:
                    
                    messagebox.showerror("Error", "La oficina ingresada no existe.")
                    self.ventana.focus()
                    return

                cursor.execute("INSERT INTO Turnos (ID, Numero_Turno, Id_Usuario, Estado, Proveedor, Fecha) VALUES (?, ?, ?, ?, ?, ?)",
                               (ID, turno, id_usuario[0], estado, proveedor, fecha))

                conn.commit()

                messagebox.showinfo("Registro", "Turno registrado exitosamente")
                self.entrada1.delete(0, END)
                self.entrada2.delete(0, END)
                self.ventana.focus()

        except pyodbc.Error as e:

            messagebox.showerror("Error de Base de Datos", f"Ocurrió un error de base de datos: {e}")
            self.ventana.focus()

        except Exception as e:
            
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

        finally:

            if conn:
                conn.close()
    