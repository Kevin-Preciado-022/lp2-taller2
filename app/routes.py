"""
Rutas (vistas) de la Tienda Virtual con consultas ORM.
"""

from flask import Blueprint, render_template, request
from .models import Producto, Categoria

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Catálogo de productos con filtro opcional por categoría (?categoria=<id>)."""
    categoria_id = request.args.get("categoria", type=int)

    if categoria_id:
        productos = Producto.query.filter_by(categoria_id=categoria_id).all()
    else:
        productos = Producto.query.all()

    categorias = Categoria.query.order_by(Categoria.nombre).all()

    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_id=categoria_id
    )


@main.route("/producto/<sku>")
def detalle(sku):
    """Detalle de un producto por SKU (error 404 si no existe)."""
    producto = Producto.query.filter_by(sku=sku).first_or_404()
    return render_template("detalle.html", producto=producto)


@main.route("/categorias")
def categorias():
    """Lista de categorías con la cantidad de productos en cada una."""
    categorias = Categoria.query.order_by(Categoria.nombre).all()
    return render_template("categorias.html", categorias=categorias)


# 🔎 Ejemplos adicionales de consultas ORM

@main.route("/productos/todos")
def todos_productos():
    """Todos los productos."""
    productos = Producto.query.all()
    return render_template("productos.html", productos=productos)


@main.route("/productos/sku/<sku>")
def producto_por_sku(sku):
    """Buscar producto por SKU (sin error automático)."""
    producto = Producto.query.filter_by(sku=sku).first()
    return render_template("detalle.html", producto=producto)


@main.route("/productos/id/<int:id>")
def producto_por_id(id):
    """Buscar producto por llave primaria."""
    producto = Producto.query.get(id)
    return render_template("detalle.html", producto=producto)


@main.route("/productos/categoria/<int:cat_id>")
def productos_por_categoria(cat_id):
    """Filtrar productos por categoría."""
    productos = Producto.query.filter_by(categoria_id=cat_id).all()
    return render_template("productos.html", productos=productos)


@main.route("/productos/ordenados")
def productos_ordenados():
    """Productos ordenados por precio."""
    productos = Producto.query.order_by(Producto.precio).all()
    return render_template("productos.html", productos=productos)


@main.route("/productos/caros")
def productos_caros():
    """Productos con precio mayor a 100000 (comparación)."""
    productos = Producto.query.filter(Producto.precio > 100000).all()
    return render_template("productos.html", productos=productos)


@main.route("/productos/contar")
def contar_productos():
    """Contar productos en la base de datos."""
    total = Producto.query.count()
    return f"Total de productos: {total}"


