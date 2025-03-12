import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter.font import BOLD
import cv2
import util.generic as utl  # Asegúrate de que este módulo exista

class ventanaTurnos:
    def actualizar_turnos(self):
        pass

    def salir(self):
        pass

    def visualizar(self):
        pass
    
    def play_video(self):
        pass
    
    def next_video(self):
        pass
    
    def play_video(self):
        pass
    
    def _get_video_files(self):
        pass

    def __init__(self):
        self.video_folder= os.path.join(os.getcwd(), "videos")
        self.video_files = self._get_video_files()
        self.current_video_index = 0
        directory = os.path.dirname(os.path.abspath(__file__))
        self.Turnos = tk.Tk()
        self.Turnos.overrideredirect(True)
        self.Turnos.title("Turnos")
        w, h = self.Turnos.winfo_screenwidth(), self.Turnos.winfo_screenheight()
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "ICONO.ico")
        self.Turnos.iconbitmap(ruta_imagen)
        self.Turnos.geometry("%dx%d+0+0" % (w, h))
        self.Turnos.resizable(1, 1)  # Permite redimensionar la ventana
        utl.centrar_ventana(self.Turnos, w, h)

        # Ventana principal
        self.frame_form = tk.Frame(self.Turnos, bd=0, relief=tk.SOLID, bg="#07a04a")
        self.frame_form.pack(expand=True, fill=tk.BOTH)

        # PARTE IZQUIERDA
        self.frame_forml = tk.Frame(self.frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        self.frame_forml.pack(side="left", expand=True, fill=tk.BOTH)

        # Etiquetas de la parte izquierda
        self.etiquetaT = tk.Label(self.frame_forml, text="Turno", font=("Arial", 20), background="#08a04b", foreground="white", width=15, height=2)
        self.etiquetaT.grid(column=1, row=0, padx=10, pady=45, sticky="ew")
        self.etiquetaO = tk.Label(self.frame_forml, text="Oficina", font=("Arial", 20), background="#08a04b", foreground="white", width=15, height=2)
        self.etiquetaO.grid(column=2, row=0, padx=10, pady=45, sticky="ew")
        self.etiquetaN = tk.Label(self.frame_forml, text="N", font=("Arial", 20), background="#08a04b", foreground="white", width=5, height=2)
        self.etiquetaN.grid(column=0, row=0, padx=10, pady=45, sticky="ew")

        # Configura las columnas para que se expandan
        self.frame_forml.grid_columnconfigure(0, weight=1)
        self.frame_forml.grid_columnconfigure(1, weight=1)
        self.frame_forml.grid_columnconfigure(2, weight=1)

        # Parte Derecha
        self.frame_formr = tk.Frame(self.frame_form, bd=0, bg="#fcfcfc")
        self.frame_formr.pack(side="right", expand=True, fill=tk.BOTH)

        # Logo
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        directorio_padre = os.path.dirname(directorio_script)
        ruta_imagen = os.path.join(directorio_padre, "imagenes", "logo.png")
        self.zapatoca = Image.open(ruta_imagen)
        self.zapatoca = self.zapatoca.resize((120, 120), Image.Resampling.LANCZOS)
        self.zapa = ImageTk.PhotoImage(master=self.frame_formr, image=self.zapatoca)
        self.label_img = tk.Label(self.frame_formr, image=self.zapa, highlightbackground="#fcfcfc", background="#fcfcfc")
        self.label_img.pack(side="top", anchor="n", pady=20)

        # Video
        self.lbvideo = tk.Label(self.frame_formr, bg="#fcfcfc")
        self.lbvideo.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        # Cargar y reproducir el primer video
        self.cap = None
        self.play_video()

        # Botón de salir
        self.boton_salir = tk.Button(self.frame_formr, text="Salir", font=("Arial", 20, BOLD), background="#08a04b", foreground="WHITE", command=self.salir)
        self.boton_salir.pack(side="bottom", anchor="se", padx=10, pady=10)
        
        self.Turnos.after(30000, self.actualizar_turnos)

        self.Turnos.mainloop()
