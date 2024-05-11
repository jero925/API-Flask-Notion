"""Definición de rutas para lógica de meses"""
from flask import Blueprint, jsonify
from ..models.meses import Meses

meses = Blueprint('meses', __name__)

@meses.route('/meses')
def get_mes_actual() -> dict:
    """Obtiene el mes actual"""
    try:
        meses_database = Meses()
        page_mes_actual: dict = meses_database.get_actual_month()
        if page_mes_actual is not None:
            return jsonify({'month': page_mes_actual, 'message': "Mes actual."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})
