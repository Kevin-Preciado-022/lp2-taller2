"""
Rutas (vistas) de la Tienda Virtual.

CAMBIO CLAVE respecto al Taller 1:
ya NO leemos productos.json en cada petición. Ahora consultamos la base de
datos a través del ORM. Las funciones cargar_productos() y
buscar_producto_por_sku() desaparecen y se reemplazan por consultas
SQLAlchemy como Producto.query.all() o Producto.query.filter_by(...).
"""

from flask import Blueprint, render_template, request
from .models import Producto, Categoria

# Definición del blueprint principal
main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Página principal: catálogo de productos desde la base de datos.
    Soporta filtro opcional por categoría mediante query string: /?categoria=<id>
    """
    # Leer parámetro ?categoria= de la URL
    categoria_id = request.args.get("categoria", type=int)

    # Filtrar productos por categoría si viene el parámetro
    if categoria_id:
        productos = Producto.query.filter_by(categoria_id=categoria_id).all()
    else:
        productos = Producto.query.all()

    # Consultar todas las categorías para el menú de filtros
    categorias = Categoria.query.order_by(Categoria.nombre).all()

    # Renderizar index.html con datos
    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_id=categoria_id
    )


@main.route("/producto/<sku>")
def detalle(sku):
    """Detalle de un producto, buscado por su SKU en la base de datos."""
    producto = Producto.query.filter_by(sku=sku).first_or_404()
    return render_template("detalle.html", producto=producto)


@main.route("/categorias")
def categorias():
    """Lista de categorías con la cantidad de productos de cada una."""
    categorias = Categoria.query.order_by(Categoria.nombre).all()
    return render_template("categorias.html", categorias=categorias)

