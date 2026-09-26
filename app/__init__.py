"""
Application factory de la Tienda Virtual (versión con base de datos).

Respecto al Taller 1, create_app() ahora también:
  - carga la configuración desde config.py
  - inicializa la extensión SQLAlchemy
  - registra los comandos de terminal (flask init-db / flask seed-db)
"""

import os

from flask import Flask

from config import Config
from .extensions import db


def create_app(config_class=Config):
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    
    app.config.from_object(config_class)

   
    os.makedirs(os.path.join(app.root_path, "..", "instance"), exist_ok=True)

   
    db.init_app(app)

   
    from . import models  # noqa: F401

    
    from .routes import main
    app.register_blueprint(main)

    
    from .commands import registrar_comandos

    registrar_comandos(app)

    return app
