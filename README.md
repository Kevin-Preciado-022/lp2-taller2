# Lenguaje de Programación 2 - Taller 2

![commits](https://badgen.net/github/commits/clubdecomputacion/lp2-taller2?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/clubdecomputacion/lp2-taller2)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor

- [Kevin Dario Preciado Vallecilla](https://github.com/Kevin-Preciado-022/lp2-taller2.git)

## Descripción del Proyecto
Este proyecto es parte del curso de Lenguajes de Programación II.
Se desarrolla una Tienda Virtual usando Python y Flask, aplicando conceptos de:

Application Factory → creación y configuración de la aplicación.

Configuración modular → separación de parámetros en config.py.

Extensiones → uso de SQLAlchemy para manejar la base de datos.

Modelos ORM → definición de tablas (Categoria, Producto).

Comandos CLI → inicialización y carga de datos (init-db, reset-db, seed-db).

Rutas y vistas → consultas ORM para mostrar productos y categorías.
## Proceso
Proceso de uso
Instalar dependencias:

pip install -r requirements.txt

Configurar la aplicación con config.py.

Inicializar la base de datos:

flask init-db

Cargar datos iniciales:

flask seed-db

Ejecutar la aplicación:

flask run

Abrir en el navegador:

http://localhost:5000

Explorar rutas principales:

/ → catálogo de productos

/producto/<sku> → detalle de producto

/categorias → lista de categorías

[GUIA.md](docs/GUIA.md)

