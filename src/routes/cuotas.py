
from flask import Blueprint, jsonify, request
from ..models.cuotas import Cuota

cuotas = Blueprint('cuotas', __name__)

@cuotas.route('/cuotas')
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
        active_dues: list = database_cuota.get_titles_rows_db(
            filters=active_filter)
        return jsonify({'month': active_dues, 'message': "Active Dues."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@cuotas.route('/cuotas/<id>')
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


@cuotas.route('/cuotas', methods=["POST"])
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
