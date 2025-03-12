import tkinter as tk
from PIL import Image, ImageTk
import src.Inicio.Inicio as Inicio
import src.conexion.Conexion as Conexion
import pyodbc
from src.Turnos.DisenoTurnos import ventanaTurnos
from gtts import gTTS
import gc
import os
import subprocess
import time
import pygame
import imutils
import cv2

class VerTurnos(ventanaTurnos):

    def __init__(self):
        self.datos_anteriores = []
        self.turnos_llamados = set()
        self.estados_anteriores = {} # Diccionario para almacenar el estado anterior de cada turno
        super().__init__()
        self.etiquetas_numero = []
        self.etiquetas_turno = []
        self.etiquetas_oficina = []
        
    def visualizar(self):
        if self.cap is not None:
            self.ret, self.frame = self.cap.read()  # Lee un frame del video
            
            if self.ret:  # Si se leyó correctamente
                self.frame = imutils.resize(self.frame, width=900)  # Redimensiona el frame
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  # Convierte de BGR a RGB
                
                self.im = Image.fromarray(self.frame)  # Convierte el frame a una imagen de PIL
                self.img = ImageTk.PhotoImage(image=self.im)  # Convierte la imagen a un formato compatible con Tkinter

                self.lbvideo.config(image=self.img)  # Actualiza la imagen en el Label
                self.lbvideo.image = self.img  # Mantén una referencia para evitar que se elimine

                # Llama a la función visualizar nuevamente después de 10 ms
                self.lbvideo.after(10, self.visualizar)
            else:
                self.next_video()
        
    def next_video(self):
        """Reproduce el siguiente video en la lista."""
        self.current_video_index += 1
        if self.current_video_index >= len(self.video_files):
            self.current_video_index = 0  # Volver al primer video si se llega al final
        self.play_video()

    def play_video(self):
        """Reproduce el video actual."""
        if self.cap is not None:
            self.cap.release()  # Liberar el video anterior

        if self.current_video_index < len(self.video_files):
            video_path = self.video_files[self.current_video_index]
            self.cap = cv2.VideoCapture(video_path)

            if not self.cap.isOpened():
                print(f"Error: No se pudo abrir el video {video_path}")
                self.next_video()  # Intentar con el siguiente video
            else:
                self.visualizar()  # Iniciar la reproducción
        else:
            print("No hay más videos en la carpeta.")

    def _get_video_files(self):
        """Obtiene la lista de archivos de video en la carpeta."""
        video_extensions = (".mp4", ".avi", ".mkv", ".mov")  # Extensiones de video soportadas
        return [
            os.path.join(self.video_folder, f)
            for f in os.listdir(self.video_folder)
            if f.lower().endswith(video_extensions)
        ]
    
    def salir(self):
        """Cierra la ventana correctamente."""
        try:
            # Cancela la operación after programada
            self.Turnos.after_cancel(self.actu_tur)
            print("Operación after cancelada")
        except Exception as e:
            # Captura cualquier error al cancelar el after
            print(f"Error al cancelar after: {e}")
        try:
            # Destruye la ventana
            self.Turnos.destroy()
            Inicio.Inicio()
            print("Ventana destruida")
        except Exception as e:
            # Captura cualquier error al destruir la ventana
            print(f"Error al destruir ventana: {e}")

        # Limpia las referencias a los widgets (opcional)
        self.etiquetas_numero = None
        self.etiquetas_turno = None
        self.etiquetas_oficina = None

        # Fuerza la recolección de basura
        gc.collect()
        print("Recolección de basura forzada")

    def _obtener_datos_turnos(self):
        """Obtiene los datos de los turnos desde la base de datos."""
        try:
            conn = Conexion.conexion()
            if conn:
                cur = conn.cursor()
                cur.execute("select T.ID, T.Proveedor, O.Nombre, T.Estado, T.Numero_Turno from Turnos as T inner join Usuarios as U on U.id=T.Id_Usuario inner join Oficina as O on U.id_oficina=O.Id where Estado='ATENDIENDO'")
                datos = cur.fetchall()
                conn.close()
                return datos
            else:
                print("Error al conectar a la base de datos")
                return []
        except pyodbc.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def _actualizar_etiquetas_turnos(self, datos):
        """Actualiza las etiquetas de los turnos con los datos proporcionados."""
        if datos == self.datos_anteriores:  # Optimización: no actualizar si los datos no han cambiado
            return

        self.datos_anteriores = datos

        # Limpiar las etiquetas existentes, excepto los encabezados
        for widget in self.frame_forml.winfo_children():
            grid_info = widget.grid_info()
            if "row" in grid_info and grid_info["row"] != 0:
                widget.grid_forget()

        self.etiquetas_numero = []
        self.etiquetas_turno = []
        self.etiquetas_oficina = []

        for i, dato in enumerate(datos):
            try:
                if len(dato) >= 5:  # Verificamos que la fila tenga al menos 5 elementos.
                    if dato[3] == "ATENDIENDO":
                        color = "white"
                    else:
                        color = "white"

                    etiqueta_numero = tk.Label(self.frame_forml, text=dato[4], font=("Arial", 20), background="#08a04b", foreground=color, width=5, height=2)
                    etiqueta_turno = tk.Label(self.frame_forml, text=dato[1], font=("Arial", 20), background="#08a04b", foreground=color, width=15, height=2)
                    etiqueta_oficina = tk.Label(self.frame_forml, text=dato[2], font=("Arial", 20), background="#08a04b", foreground=color, width=15, height=2)

                    etiqueta_numero.grid(column=0, row=i + 2, padx=10, pady=10, sticky="ew")
                    etiqueta_turno.grid(column=1, row=i + 2, padx=10, pady=10, sticky="ew")
                    etiqueta_oficina.grid(column=2, row=i + 2, padx=10, pady=10, sticky="ew")

                    self.etiquetas_numero.append(etiqueta_numero)
                    self.etiquetas_turno.append(etiqueta_turno)
                    self.etiquetas_oficina.append(etiqueta_oficina)
                else:
                    print(f"fila incorrecta: {dato}")

            except IndexError as e:
                print(f"Error de índice en la fila {i}: {e}, contenido de la fila: {dato}")
            except Exception as e:
                print(f"Otro error en la fila {i}: {e}, contenido de la fila: {dato}")

    # ... (resto de tu código, incluyendo self.Turnos y otras definiciones)

    def _generar_voz(self, texto, callback=None):
        """Genera un archivo de audio con el texto proporcionado."""
        try:
            ruta_archivo = os.path.abspath("turno.mp3")
            tts = gTTS(text=texto, lang='es')
            tts.save("turno.mp3")

            pygame.mixer.init()
            pygame.mixer.music.load(ruta_archivo)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            pygame.mixer.music.unload()
            os.remove(ruta_archivo)

            if callback:
                
                self.Turnos.after(1000, callback)
                
        except Exception as e:
            print(f"Error al generar voz: {e}")

    def actualizar_turnos(self):
        """Actualiza la interfaz con los datos de los turnos."""
        try:
            datos = self._obtener_datos_turnos()
            print("Datos obtenidos:", datos)  # Verificar datos obtenidos
            self._actualizar_etiquetas_turnos(datos)

            # Limpiar turnos_llamados
            ids_actuales = {dato[0] for dato in datos}
            self.turnos_llamados = {id_turno for id_turno in self.turnos_llamados if id_turno in ids_actuales}

            # Actualizar turnos_llamados basado en cambios de estado
            for dato in datos:
                dato_id = dato[0]
                estado_actual = dato[3]
                if dato_id in self.estados_anteriores:
                    estado_anterior = self.estados_anteriores[dato_id]
                    if estado_actual == "ATENDIENDO" and estado_anterior != "ATENDIENDO":
                        self.turnos_llamados.add(dato_id)
                    elif estado_actual != "ATENDIENDO" and estado_anterior == "ATENDIENDO":
                        self.turnos_llamados.discard(dato_id)
                self.estados_anteriores[dato_id] = estado_actual

            # Generar voz para cada turno nuevo
            def generar_siguiente(datos, index=0):
                print("generar_siguiente llamado:", index)  # Verificar la llamada de la función
                if index < len(datos):
                    dato = datos[index]
                    numero_turno = dato[4]
                    dato_id = dato[0]
                    print("Index:", index, "Dato ID:", dato_id)  # Verificar index y dato_id
                    if dato_id not in self.turnos_llamados:
                        print("Turnos llamados:", self.turnos_llamados)  # Verificar turnos llamados
                        texto_turno = f"Atención, turno: {numero_turno}. Por favor, diríjase a la oficina de {dato[2]}."
                        self._generar_voz(texto_turno, lambda: generar_siguiente(datos, index + 1))
                        print("Llamada a generar siguiente desde callback")  # Verificar llamada desde callback
                        self.turnos_llamados.add(dato_id)
                    else:
                        generar_siguiente(datos, index + 1)
                else:
                    self.actu_tur = self.Turnos.after(30000, self.actualizar_turnos)

            generar_siguiente(datos)

        except Exception as e:
            print(f"Ocurrió un error: {e}")
            self.actu_tur = self.Turnos.after(30000, self.actualizar_turnos)