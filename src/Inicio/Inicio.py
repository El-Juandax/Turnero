import tkinter as tk
import tkinter.messagebox as messageBox
import sys
import util.generic as utl
from src.Inicio.InicioDiseno import Inicio  # Asegúrate de que la importación sea correcta
from src.login.Ingreso import Ingreso
from src.usuario.usuario import Usuario
from src.Asignar.AsignarT import Asignar
from src.Turnos.Turnos import VerTurnos

class Inicio(Inicio):  # Asumiendo que Inicio es tu clase de diseño

    def __init__(self):
        super().__init__()

    def navegar(self):
        self.ventanaI.destroy()
        Ingreso()

    def navegarA(self):
        self.ventanaI.destroy()
        Asignar()

    def navegarT(self):
        self.ventanaI.destroy()
        VerTurnos()

    def salir(self):
        pregunta = messageBox.askquestion("Salir", "¿Desea salir de la aplicación?")
        
        if pregunta == "yes":
            
            self.ventanaI.destroy()
            print("Aplicación cerrada.")
            sys.exit()
            
        else:
            pass


    










































"""# ventana Inicio -------------------------------------------------------------------------------------------------------
def asignar():
    ventana.withdraw
    AsignarT.AsignarV()


def turnos():
    ventana.withdraw()
    Turnos.ventanaTurnos()  
    
def navegarIngreso():
    ventana.withdraw()
    Ingreso.ventanaIngreso()
    
def salir():
    
    respuesta = tkinter.messagebox.askquestion("Salir", "Esta seguro que desea salir?")
    
    if respuesta == "yes":
       ventana.destroy()
       Ingreso.salir()
       Turnos.salir()
    else:
       pass

def ventanaInicio():
    
    global ventana
    ventana = Tk()
    ventana.update()
    ventana.title("Inicio")

    anv = ventana.winfo_screenwidth()
    alv = ventana.winfo_screenheight()
    anp = ventana.winfo_screenwidth()
    alp = ventana.winfo_screenheight()

    x = (anv-anp)/2
    y = (alv-alp)/2

    ventana.geometry('%dx%d+%d+%d'%(anp,alp,x,y))

    etiqueta = Label(ventana, text="Bienvenido a la aplicación de gestión de turnos", font=("Arial", 20))
    etiqueta.grid(row=0, column=10, pady=90, padx=380)

    boton1=Button(ventana, text="Ingresar al sistema", command=navegarIngreso, width=30, height=2)
    boton1.grid(row=2, column=10, pady=20, padx=380 )
    boton2=Button(ventana, text="Asignar turnos", command=asignar, width=30, height=2)
    boton2.grid(row=3, column=10, pady=20, padx=380 )
    boton3=Button(ventana, text="Ver turnos", command=turnos, width=30, height=2)
    boton3.grid(row=4, column=10, pady=20, padx=380 )
    boton4=Button(ventana, text="Salir", command=salir, width=30, height=2)
    boton4.grid(row=5, column=10, pady=20, padx=380)

    ventana.mainloop()"""