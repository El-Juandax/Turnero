import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
import os


class Inicio:

    def navegar(self):
        pass

    def navegarA(self):
        pass

    def navegarT(self):
        pass

    def salir(self):
        self.ventanaI.destroy()

    def __init__(self):
        self.ventanaI = tk.Tk()
        self.ventanaI.title("Inicio")
        self.ventanaI.state("zoomed")
        w, h = self.ventanaI.winfo_screenwidth(), self.ventanaI.winfo_screenheight()
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "ICONO.ico")
        try:
            self.ventanaI.iconbitmap(ruta_imagen)
        except tk.TclError:
            print(f"No se pudo cargar el icono desde: {ruta_imagen}")

        self.ventanaI.geometry("%dx%d+0+0" % (w, h))
        self.ventanaI.resizable(1,1)

        utl.centrar_ventana(self.ventanaI, w, h)

        # Ventana formulario
        frame_form = tk.Frame(self.ventanaI, bd=0, relief=tk.SOLID)
        frame_form.pack(fill=tk.BOTH, expand=tk.YES, pady=130)

        # Cabecera
        frame_form_top = tk.Frame(frame_form, height=100, width=100)
        frame_form_top.pack(side="top")
        title = tk.Label(frame_form_top, text="Bienvenido a la aplicación de gestión de turnos", font=('Arial narrow', 20, BOLD), pady=100)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # Contenido
        frame_form_content = tk.Frame(frame_form, height=100, bd=0, width=0, relief=tk.SOLID)
        frame_form_content.pack(side="top", fill=tk.Y, expand=tk.YES)

        # Configurar las columnas y filas para que se expandan
        frame_form_content.grid_columnconfigure(0, weight=0)
        frame_form_content.grid_rowconfigure(0, weight=0)
        frame_form_content.grid_rowconfigure(1, weight=0)
        frame_form_content.grid_rowconfigure(2, weight=0)
        frame_form_content.grid_rowconfigure(3, weight=0)

        # Botones
        boton1 = tk.Button(frame_form_content, text="Ingresar al sistema", command=self.navegar, width=40, height=2, bg="#07a04a", bd=0, font=('arial', 11, BOLD), foreground="white")
        boton1.grid(row=0, column=0,  padx=200, pady=5)

        boton2 = tk.Button(frame_form_content, text="Asignar turnos", command=self.navegarA, width=40, height=2, bg="#07a04a", bd=0, font=('arial', 11, BOLD), foreground="white")
        boton2.grid(row=1, column=0,  padx=200, pady=5)

        boton3 = tk.Button(frame_form_content, text="Ver turnos", command=self.navegarT, width=40, height=2, bg="#07a04a", bd=0, font=('arial', 11, BOLD), foreground="white")
        boton3.grid(row=2, column=0,  padx=200, pady=5)

        boton4 = tk.Button(frame_form_content, text="Salir", command=self.salir, width=40, height=2, bg="#07a04a", bd=0, font=('arial', 11, BOLD), foreground="white")
        boton4.grid(row=3, column=0,  padx=200, pady=5)

        # Atajos de teclado
        self.ventanaI.bind("<Control-i>", lambda event: self.navegar())
        self.ventanaI.bind("<Control-a>", lambda event: self.navegarA())
        self.ventanaI.bind("<Control-t>", lambda event: self.navegarT())
        self.ventanaI.bind("<Control-s>", lambda event: self.salir())

        self.ventanaI.mainloop()
