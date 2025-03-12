from PIL import Image, ImageTk

def leer_imagen(nombre, tamano):
    return ImageTk.PhotoImage(Image.open(nombre).resize(tamano, Image.Resampling.LANCZOS))

def centrar_ventana(ventana, ancho, alto):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_alto = ventana.winfo_screenheight()
    x = int((pantall_ancho / 2) - (ancho / 2))
    y = int((pantall_alto / 2) - (alto / 2))
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
