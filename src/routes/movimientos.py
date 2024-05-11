"""Definición de rutas para lógica de movimientos"""
from flask import Blueprint, jsonify, request
from ..models.flujo_plata import FlujoPlata

movimientos = Blueprint('movimientos', __name__)

@movimientos.route('/movimientos', methods=["POST"])
def add_new_transaction() -> None:
    """
    Agrega un nuevo producto en cuotas a la base de datos.

    Returns:
        None. Retorna un mensaje JSON indicando el resultado de la operación.
    """
    try:
        # print(request.args)
        # print(request.json)
        database_flujo_plata: FlujoPlata = FlujoPlata()

        flujo_plata_props_body: dict = {
            "icon": request.json["icon"],
            "Nombre": request.json["name"],
            "Monto": request.json["monto"],
            "I/O": request.json["i_o"],
            "Fecha": request.json["fecha"],
            "Cuenta": request.json["cuenta"],
            "Gasto. Mes Año": request.json.get("gasto_mes", ""),
            "Ingreso. Mes Año": request.json.get("ingreso_mes", ""),
            "Tipo": request.json["tipo"]
        }
        database_flujo_plata.create_page(props_modified=flujo_plata_props_body)
        return jsonify({'message': "Nuevo movimiento agregado."})
    except Exception as ex:
        return jsonify({'message': f"Error al el movimiento: \n {ex}"})
