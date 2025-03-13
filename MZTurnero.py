from src.Inicio.Inicio import Inicio


def main():
    try:
        Inicio()
    except Exception as e:
        
        print(f'Ha ocurrido un error inesperado: {e}')

if __name__ == '__main__':
    main()

# pyinstaller --onefile --add-data "src;src" --windowed --icon=src/imagenes/ICONO.ico  MZTurnero.py 
# python -m pip freeze > requirements.txt
