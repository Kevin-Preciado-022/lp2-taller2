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
    
        """Crea todas las tablas definidas en models.py."""
        # TODO 1: Llama a db.create_all() para crear las tablas.
        db.create_all()
        # TODO 2: Muestra un mensaje de confirmación con click.echo(...)
        click.echo("✅ Tablas creadas ")
        pass

    @app.cli.command("reset-db")
    def reset_db():
        """Borra y vuelve a crear todas las tablas (¡pierde los datos!)."""
        # TODO 3: Llama a db.drop_all() y luego a db.create_all()
        db.drop_all()
        db.create_all()
        # TODO 4: Muestra un mensaje de confirmación
        click.echo ("Base de datos reiniciada: tablas borradas y recreadas.")
        pass

    @app.cli.command("seed-db")
    def seed_db():
        """Carga los productos de productos.json en la base de datos."""

        # --- Leer el archivo JSON -------------------------------------
        # TODO 5: Abre RUTA_PRODUCTOS con encoding="utf-8" y usa
        #         json.load() para obtener la lista de productos.
        # datos = ...
        with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        cargados = 0

        # --- Insertar categorías y productos 
        # --------------------------
        for item in datos:
            # TODO 6: Buscar si su categoría ya existe en la base de datos:
            categoria = Categoria.query.filter_by(nombre=item["categoria"]).first()

            # TODO 7: Si no existe, crearla y agregarla a la sesión:
            if not categoria:
                categoria = Categoria(nombre=item["categoria"])
                db.session.add(categoria)
                db.session.flush()  # asigna el id sin confirmar aún

            # TODO 8: Evitar duplicados: si ya existe un Producto con ese sku
            if Producto.query.filter_by(sku=item["sku"]).first():
                continue

            # TODO 9: Crear el objeto Producto con los datos del JSON y
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
        ---------------------------------
        # TODO 10: Llama a db.session.commit() para guardar TODO de una
        #          vez. Hasta este momento nada se ha escrito en disco.
        db.session.commit()

        # TODO 11: Muestra cuántos productos se cargaron con click.echo(...)
        click.echo(f"✅ {cargados} productos cargados.")
