"""Definición de rutas para lógica de cuentas"""
from flask import Blueprint, jsonify, request
from ..models.payment_methods import MetodoPago

cuentas = Blueprint('cuentas', __name__)

@cuentas.route('/cuentas')
def get_all_payment_methods() -> dict:
    """Obtiene un listado de diccionarios con Id y Nombre de las cuentas"""
    try:
        cuentas_database = MetodoPago()
        payment_methods_data: dict = cuentas_database.get_titles_rows_db()
        if payment_methods_data is not None:
            return jsonify({'payment_methods': payment_methods_data,
                            'message': "Cuentas obtenidas correctamente."})
        else:
            return jsonify({'message': "No se han encontrado datos."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@cuentas.route('/cuentas/<id>')
def get_payment_method(id: str) -> dict:
    """Obtiene un listado de diccionarios con Id y Nombre de las cuentas"""
    try:
        cuentas_database = MetodoPago()
        payment_methods_data: dict = cuentas_database.get_page_by_id(id)
        if payment_methods_data is not None:
            return jsonify({'payment_method': payment_methods_data,
                            'message': "Cuenta obtenidas correctamente."})
        else:
            return jsonify({'message': "No se han encontrado datos."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})
