"""Rutas de mi aplicacion"""
from flask import Flask
from flask_cors import CORS, cross_origin

from src.routes.cuotas import cuotas
from src.routes.meses import meses
from src.routes.cuentas import cuentas
from src.routes.movimientos import movimientos
from src.routes.users_angular import users

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    """Pagina de inicio"""
    return "<h1>Hola Mundo</h1>"

app.register_blueprint(cuotas)
app.register_blueprint(meses)
app.register_blueprint(cuentas)
app.register_blueprint(movimientos)
app.register_blueprint(users)

def error_not_found(error):
    """Para gestionar casos de error"""
    return f"<h1>No existe la pagina...</h1> \n {error}", 404


if __name__ == "__main__":
    app.register_error_handler(404, error_not_found)
    app.run(debug=True)
