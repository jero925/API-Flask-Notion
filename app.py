"""Rutas de mi aplicacion"""
from flask import Flask

from src.routes.cuotas import cuotas
from src.routes.meses import meses
from src.routes.cuentas import cuentas
from src.routes.movimientos import movimientos

app = Flask(__name__)


@app.route('/')
def index():
    """Pagina de inicio"""
    return "<h1>Hola Mundo</h1>"

app.register_blueprint(cuotas)
app.register_blueprint(meses)
app.register_blueprint(cuentas)
app.register_blueprint(movimientos)

def error_not_found(error):
    """Para gestionar casos de error"""
    return f"<h1>No existe la pagina...</h1> \n {error}", 404


if __name__ == "__main__":
    app.register_error_handler(404, error_not_found)
    app.run(debug=True, port=3000)
