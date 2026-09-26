"""
Configuración de la aplicación.

Separar la configuración del código de la aplicación es una buena práctica:
permite tener valores distintos para desarrollo, pruebas y producción sin
tocar la lógica del programa.
"""

import os

# Ruta absoluta a la carpeta raíz del proyecto (donde está run.py).
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuración base (desarrollo)."""

    
    SECRET_KEY =  os.environ.get("SECRET_KEY", "Cielo_Rojo_22046")

    
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR, "instance", "tienda.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ECHO = False
