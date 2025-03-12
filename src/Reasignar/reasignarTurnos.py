from tkinter import *
from src.Reasignar.disenoReasignar import DisenoReasignar
import src.conexion.Conexion as Conexion
import src.Asignar.AsignarT as Asignar
import tkinter.messagebox as MessageBox

class Reasignar(DisenoReasignar):
    
    def my_upper(self, *args):
        self.string.get(self.string.get().upper())
        
    def my_upper2(self, *args):
        self.string2.get(self.string2.get().upper())
        
    def actu_dinamica(self, event):
        self.texto_ingresado1 = self.entrada2.get()
        self.opciones_filtradas1 =  [opcion1 for opcion1 in self.oficinas if self.texto_ingresado1 in opcion1]
        self.entrada2['values'] = self.opciones_filtradas1
        
    def reasignar(self):
        
        pregunta = MessageBox.askquestion("Reasignar", "¿Esta seguro de reasignar el turno?")
        
        if pregunta == "yes":
            
            fecha = self.entrada3.get()
            conn= Conexion.conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT U.id, U.id_Oficina from Usuarios as U inner join Oficina as O on U.id_oficina=O.Id where O.Nombre=?", (self.entrada2.get()))
            idU = cursor.fetchone()
            ID = str(idU[0]) + str(self.entrada1.get()) + str(fecha.replace("/", ""))
            cursor.execute("UPDATE Turnos SET Id_Usuario=? WHERE Id=?", (idU[0], ID))
            cursor.commit()
            cursor.close()
            conn.close()
            MessageBox.showinfo("Reasignar", "Turno reasignado correctamente")
            
            self.entrada1.delete(0, END)
            self.entrada2.delete(0, END)
            self.entrada3.delete(0, END)
            self.ventana.focus()
        
        else:
            pass
         
    def salir(self):
        self.ventana.destroy()
        Asignar.Asignar()
         
    def __init__(self):
        super().__init__()