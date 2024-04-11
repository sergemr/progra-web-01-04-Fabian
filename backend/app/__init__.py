import os
from flask import Flask
from .modelos import db  
from os import getenv  
from dotenv import load_dotenv  
from flask_jwt_extended import JWTManager  

# Importar los blueprints (componentes) de la aplicación
from backend.api.usuarios import usuarios_bp
from backend.api.productos import productos_bp

# Definir la función para crear y configurar la instancia de la aplicación Flask
def crear_app(environment=None):
    app = Flask(__name__)  # Crear una nueva instancia de la aplicación Flask

    # Cargar las variables de entorno desde un archivo .env, si está presente
    load_dotenv()
    # Si se proporciona un nombre de entorno, configurarlo como una variable de entorno
    if(environment != None):
        os.environ['ENTORNO_FLASK'] = environment

    # Cargar el objeto de configuración apropiado basado en el entorno actual
    if getenv('ENTORNO_FLASK') == 'desarrollo':
        from backend.config.db_config import Desarrollo as Config
    elif getenv('ENTORNO_FLASK') == 'produccion':
        from backend.config.db_config import Produccion as Config
    elif getenv('ENTORNO_FLASK') == 'staging':
        from backend.config.db_config import Staging as Config
    elif getenv('ENTORNO_FLASK') == 'pruebas-caja-arena':
        from backend.config.db_config import PruebasEfimeras as Config
    elif getenv('ENTORNO_FLASK') == 'pruebas':
        from backend.config.db_config import Pruebas as Config
    else:
        # Levantar una excepción si la variable de entorno no está configurada o tiene un valor inválido
        raise ValueError("Valor de la variable de ambiente ENTORNO_FLASK incorrecto o no configurado. ¿Olvidaste definirlo en tu archivo .env? ¿Es el valor correcto?")

    # Cargar la configuración del objeto config seleccionado en la instancia de la aplicación Flask
    app.config.from_object(Config)
    # Inicializar la base de datos con la instancia de la aplicación Flask
    db.init_app(app)

    # Registrar blueprints (componentes) con la instancia de la aplicación Flask
    app.register_blueprint(usuarios_bp)  # Registrar el blueprint de usuarios con un prefijo de URL
    app.register_blueprint(productos_bp)

    # Inicializar Flask-JWT-Extended con la instancia de la aplicación Flask
    JWTManager(app)
    
    return app  # Devolver la instancia de la aplicación Flask configurada