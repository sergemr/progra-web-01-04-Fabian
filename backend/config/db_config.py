import os
from dotenv import load_dotenv

# Carga variables de entorno
load_dotenv()

class Config(object):
    # Configuración base para la aplicación Flask, incluye claves secretas y conexión a la base de datos.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

    if JWT_SECRET_KEY is None:
        raise ValueError("No se ha configurado JWT_SECRET_KEY para la aplicación Flask. ¿Olvidaste definirlo en tu archivo .env?")

    SEGUIMIENTO_MODIFICACIONES_SQLALCHEMY = False
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('URL_BASE_DE_DATOS')
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("No se ha configurado URL_BASE_DE_DATOS para la aplicación Flask. ¿Olvidaste definirlo en tu archivo .env?")

class Desarrollo(Config):
    # Configuración específica para el entorno de desarrollo, incluye depuración y registro de SQL.
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Habilita registro de consultas SQL

class Produccion(Config):
    # Configuración para el entorno de producción, deshabilita la depuración.
    DEBUG = False

class Staging(Config):
    # Configuración para el entorno de staging, similar a producción pero puede incluir diferencias menores.
    DEBUG = False

class PruebasEfimeras(Config):
    # Configuración para pruebas efímeras, con base de datos de sandbox.
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('URL_BASE_DE_DATOS_SANDBOX')
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("No se ha configurado URL_BASE_DE_DATOS_SANDBOX para la aplicación Flask. ¿Olvidaste definirlo en tu archivo .env?")

class Pruebas(Config):
    # Configuración para el entorno de pruebas, con base de datos específica para pruebas.
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('URL_BASE_DE_DATOS_PRUEBAS')
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("No se ha configurado URL_BASE_DE_DATOS_PRUEBAS para la aplicación Flask. ¿Olvidaste definirlo en tu archivo .env?")