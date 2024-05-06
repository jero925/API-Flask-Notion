"""Rutas de mi aplicacion"""
from flask import Flask, jsonify, request
# from src.models.database_model import FlujoPlata
from src.models.cuotas import Cuota
from src.models.meses import Meses

app = Flask(__name__)


@app.route('/')
def index():
    """Pagina de inicio"""
    return "<h1>Hola Mundo</h1>"

# GET


@app.route('/cuotas')
def get_cuotas() -> dict:
    """Obtiene cuotas activas"""
    try:
        database_cuota: Cuota = Cuota()
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
        active_dues: list = database_cuota.get_titles_rows_db(filters=active_filter)
        return jsonify({'month': active_dues, 'message': "Active Dues."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@app.route('/cuotas/<id>')
def get_cuota_by_id(id: str) -> dict:
    """Obtiene una cuota específica"""
    try:
        database_cuota: Cuota = Cuota()

        page_cuota_data = database_cuota.get_page_by_id(id)
        if page_cuota_data is not None:
            return jsonify({'due': page_cuota_data, 'message': "Cuota obtenida exitosamente."})
        else:
            return jsonify({'message': "Cuota no encontrada."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})

@app.route('/meses')
def get_mes_actual() -> dict:
    """Obtiene el mes actual"""
    try:
        database_meses = Meses()
        page_mes_actual: dict = database_meses.get_actual_month()
        if page_mes_actual is not None:
            return jsonify({'month': page_mes_actual, 'message': "Mes actual."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})

# POST

@app.route('/cuota', methods=["POST"])
def add_new_due_product() -> dict:
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


# @app.route('/movimiento', methods=["POST"])
# def add_new_transaction() -> None:
#     """
#     Agrega un nuevo producto en cuotas a la base de datos.

#     Returns:
#         None. Retorna un mensaje JSON indicando el resultado de la operación.
#     """
#     try:
#         # print(request.args)
#         # print(request.json)
#         database_flujo_plata: FlujoPlata = FlujoPlata()

#         flujo_plata_props_body: dict = {
#             "icon": request.json["icon"],
#             "Nombre": request.json["name"],
#             "Monto": request.json["monto"],
#             "I/O": request.json["i_o"],
#             "Fecha": request.json["fecha"],
#             "Cuenta": request.json["cuenta"],
#             "Gasto. Mes Año": request.json.get("gasto_mes", ""),
#             "Ingreso. Mes Año": request.json.get("ingreso_mes", ""),
#             "Tipo": request.json["tipo"]
#         }
#         database_flujo_plata.create_page(props_modified=flujo_plata_props_body)
#         return jsonify({'message': "Nuevo movimiento agregado."})
#     except Exception as ex:
#         return jsonify({'message': f"Error al el movimiento: \n {ex}"})

def error_not_found(error):
    """Para gestionar casos de error"""
    return f"<h1>No existe la pagina...</h1> \n {error}", 404


if __name__ == "__main__":
    app.register_error_handler(404, error_not_found)
    app.run(debug=True, port=3000)
