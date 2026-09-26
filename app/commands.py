"""
Comandos personalizados de terminal (Flask CLI).

Permiten ejecutar tareas administrativas desde la terminal, por ejemplo:

    flask init-db     -> crea las tablas en la base de datos
    flask seed-db     -> carga los productos del JSON a la base de datos

Estos comandos se registran en create_app().
"""

import json
import os

import click

from .extensions import db
from .models import Categoria, Producto

RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "data", "productos.json")


def registrar_comandos(app):
    """Asocia los comandos a la aplicación Flask recibida."""

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        click.echo("Tablas creadas ")
        pass

    @app.cli.command("reset-db")
    def reset_db():
        """Borra y vuelve a crear todas las tablas (¡pierde los datos!)."""
        
        db.drop_all()
        db.create_all()
        
        click.echo ("Base de datos reiniciada: tablas borradas y recreadas.")
        pass

    @app.cli.command("seed-db")
    def seed_db():
        """Carga los productos de productos.json en la base de datos."""

       
        with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        cargados = 0

       
        for item in datos:
           
            categoria = Categoria.query.filter_by(nombre=item["categoria"]).first()

            if not categoria:
                categoria = Categoria(nombre=item["categoria"])
                db.session.add(categoria)
                db.session.flush()  # asigna el id sin confirmar aún

            if Producto.query.filter_by(sku=item["sku"]).first():
                continue

           
            producto = Producto(
                sku=item["sku"],
                marca=item["marca"],
                nombre=item["nombre"],
                precio=item["precio"],
                foto=item.get("foto"),
                stock=item.get("stock", 0),
                activo=item.get("activo", True),
                categoria_id=categoria.id,
            )
            db.session.add(producto)
            cargados += 1
        
        db.session.commit()

       
        click.echo(f"✅ {cargados} productos cargados.")
