"""Rutas de mi aplicacion"""
import os
from flask import Flask, jsonify, request
from models.database_model import Database, Cuota

app = Flask(__name__)


@app.route('/')
def index():
    """Pagina de inicio"""
    return "<h1>Hola Mundo</h1>"

# GET


@app.route('/cuotas')
def get_cuotas():
    """Obtiene cuotas activas"""
    try:
        database_cuota: Database = Database(
            database_id=os.getenv("CUOTAS_DB_ID"), name="Cuota")
        active_filter: dict = {
            "and": [
                {
                    "property": "Activa",
                    "checkbox": {
                        "equals": True
                    }
                }
            ]
        }
        active_dues: list = database_cuota.get_names_rows_db(
            filters=active_filter)
        return jsonify({'dues': active_dues, 'message': "Active Dues."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@app.route('/cuotas/<id>')
def get_cuota_by_id(id: str) -> None:
    """Obtiene una cuota específica"""
    try:
        database_cuota: Database = Database(
            database_id=os.getenv("CUOTAS_DB_ID"), name="Cuota")

        page_cuota_data = database_cuota.get_page_by_id(id)
        if page_cuota_data is not None:
            return jsonify({'due': page_cuota_data, 'message': "Cuota obtenida exitosamente."})
        else:
            return jsonify({'message': "Cuota no encontrada."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})

# POST


@app.route('/cuota', methods=["POST"])
def add_new_due_product() -> None:
    """
    Agrega un nuevo producto en cuotas a la base de datos.

    Returns:
        None. Retorna un mensaje JSON indicando el resultado de la operación.
    """
    try:
        # print(request.args)
        # print(request.json)
        database_cuota: Cuota = Cuota()

        cuota_props_body: dict = {
            "icon": "",
            "Name": request.json["name"],
            "Monto Total": request.json["monto total"],
            "Cantidad de cuotas": request.json["cantidad de cuotas"],
            "Primer cuota": request.json["primer cuota"],
            "Fecha de compra": request.json["fecha de compra"],
            "Meses": request.json["meses"]
        }
        database_cuota.create_page(props_modified=cuota_props_body)
        return jsonify({'message': "Producto en cuotas agregado."})
    except Exception as ex:
        return jsonify({'message': f"Error al registrar nueva cuota. \n {ex}"})


def error_not_found(error):
    """Para gestionar casos de error"""
    return f"<h1>No existe la pagina...</h1> \n {error}", 404


if __name__ == "__main__":
    app.register_error_handler(404, error_not_found)
    app.run(debug=True, port=3000)
