import pyodbc

def conexion():
    try:
        # Conexión a la base de datos
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.99\ICG;DATABASE=Turnero;UID=sa;PWD=abc123')
        return conn
    
    except Exception as e: 
        
        print("Error al conectar a la base de datos:", e)
        return None

        
