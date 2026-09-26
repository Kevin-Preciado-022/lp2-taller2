"""
Punto de entrada de la aplicación.

Ejecutar con:
    python run.py

O usando el CLI de Flask (necesario para los comandos init-db / seed-db):
    export FLASK_APP=run.py
    flask run
"""

from app import create_app
from app.extensions import db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Objetos disponibles automáticamente al ejecutar 'flask shell'.

    Esto te permite probar consultas del ORM sin importar nada a mano:
        $ flask shell
        >>> Producto.query.all()
    """
    from app.models import Producto, Categoria

    
    return {"db": db, "Producto": Producto, "Categoria": Categoria} 
    pass


if __name__ == "__main__":
    app.run(debug=True)
    pass
