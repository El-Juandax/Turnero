import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from tkinter.font import BOLD
import os

class DisenoUsuario:
    def salir(self):
        pass

    def mostrar_datos(self):
        pass

    def Turnos(self):
        pass

    def siguienteT(self):
        pass

    def reanudar(self):
        pass

    def detener(self):
        pass

    def seleccion_tabla(self):
        pass

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Usuario")
        self.ventana.state("zoomed")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.resizable(1, 1)
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "ICONO.ico")
        self.ventana.iconbitmap(ruta_imagen)
        self.ventana.config(background="#365633")
        utl.centrar_ventana(self.ventana, w, h)  # Asumiendo que esta función ya está definida.

        # ventana
        frame_form = tk.Frame(self.ventana, background="#a8e4ae")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)
        self.label = ttk.Label(frame_form, text="Usuario", font=("Arial ", 20, BOLD), foreground="black", background="#a8e4ae")
        self.mostrar_datos()  # Asumiendo que esta función ya está definida.
        self.label.pack(pady=10)
        self.exit = tk.Button(frame_form, text="Salir", font=("Arial", 12, BOLD), bd=0, background="#a8e4ae", command=self.salir)
        self.exit.place(x=10, y=10)
        self.exit.bind("<Return>", (lambda event: self.salir()))
        # ventana

        # Contenedor
        frame_form_center = tk.Frame(frame_form, background="#579053")
        frame_form_center.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.43, relheight=0.8)  # Ajuste aquí

        frame_form_content = tk.Frame(frame_form_center, background="#579053")
        frame_form_content.pack(expand=tk.YES, fill=tk.BOTH, padx=40, pady=20)

        self.label1 = ttk.Label(frame_form_content, text="TURNO", font=("Arial narrow", 20, BOLD), width=12, anchor=tk.CENTER, foreground="white", background="#579053")
        self.label1.grid(column=0, row=0, padx=20, pady=30)
        self.label2 = ttk.Label(frame_form_content, text="PROVEEDOR", font=("Arial narrow", 20, BOLD), width=12, anchor=tk.CENTER, foreground="white", background="#579053")
        self.label2.grid(column=1, row=0, padx=0, pady=10)

        self.Codigo = ttk.Label(frame_form_content, font=("Arial", 20, BOLD), width=12, anchor=tk.CENTER, borderwidth=2, relief="solid", background="white")
        self.Codigo.grid(column=0, row=1, padx=10, pady=15)
        self.Proveedor = ttk.Label(frame_form_content, font=("Arial", 20, BOLD), width=12, anchor=tk.CENTER, borderwidth=2, relief="solid", background="white")
        self.Proveedor.grid(column=1, row=1)
        self.id = ttk.Label(frame_form_content, font=("Arial", 20, BOLD), width=12, anchor=tk.CENTER, borderwidth=2, relief="solid", background="white")

        self.Turnos() # Asumiendo que esta función ya está definida.

        self.boton = tk.Button(frame_form_content, font=("Arial narrow", 20, BOLD), command=self.siguienteT, text="SIGUIENTE", foreground="#0f4d0a", bd=0, background="#a8e4ae")
        self.boton.grid(column=0, row=2, pady=25)
        self.boton2 = tk.Button(frame_form_content, font=("Arial narrow", 20, BOLD), command=self.detener, text="TERMINAR", foreground="#0f4d0a", bd=0, background="#a8e4ae")
        self.boton2.grid(column=1, row=2, pady=25)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial narrow", 22, BOLD))
        style.configure("Treeview", font=("Arial narrow", 18, BOLD), rowheight=30) 
        
        self.scrollbar = ttk.Scrollbar(frame_form_content, orient=tk.VERTICAL)
        self.tabla = ttk.Treeview(frame_form_content, columns=("Numero Turno", "Proveedor"), show="headings", yscrollcommand=self.scrollbar.set,)
        self.tabla.heading("Numero Turno", text="Numero Turno")
        self.tabla.heading("Proveedor", text="Proveedor")
        self.tabla.column("Numero Turno", anchor=tk.CENTER)
        self.tabla.column("Proveedor", anchor=tk.CENTER)
       
        
        self.seleccion_tabla()

        self.scrollbar.config(command=self.tabla.yview)

        # Usar grid para la disposición
        self.scrollbar.grid(row=3, column=2, sticky='ns')  # Columna 2, sticky 'ns' para estirar verticalmente
        self.tabla.grid(row=3, column=0, columnspan=2, sticky='nsew') # Columna 0 y 1, sticky 'nsew' para estirar en todas las direcciones

        # Configurar el peso de las filas y columnas para que la tabla se expanda correctamente
        frame_form_content.grid_rowconfigure(3, weight=1)
        frame_form_content.grid_columnconfigure(0, weight=1)
        frame_form_content.grid_columnconfigure(1, weight=1)

        self.ventana.mainloop()

if __name__ == "__main__":
    app = DisenoUsuario()
        