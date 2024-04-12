from backend.app import crear_app, db
from sqlalchemy import text
from flask_cors import CORS  # Importar CORS para manejar el intercambio de recursos de origen cruzado

# Crear una instancia de la aplicación con el entorno de desarrollo
app = crear_app('desarrollo')

# Aplicar middleware CORS a la aplicación para permitir solicitudes de origen cruzado
CORS(app)

# Crear tablas de base de datos dentro del contexto de la aplicación
with app.app_context():
    db.drop_all()  # Now you can drop all tables
    db.create_all()  # And create them again


# Definir una ruta raíz que devuelva un saludo
@app.route('/')
def index():
    return "Hello, your Flask app is running!"

# Ejecutar la aplicación en modo de depuración si este script es el punto de entrada principal
if __name__ == "__main__":
    app.run(debug=True)
