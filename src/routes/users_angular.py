"""Definición de rutas para lógica de movimientos"""
from flask import Blueprint, jsonify, request
from ..models.users_angular import UsuarioAngular
from src.utils.security import Security
users = Blueprint('users', __name__)

# @users.route('/users')
# def get_users() -> dict:
#     """Obtien toda la lista de usuarios"""
#     try:
#         database_cuota: Cuota = Cuota()
#         active_filter: dict = {
#             "and": [
#                 {
#                     "property": "Activa",
#                     "checkbox": {
#                         "equals": True
#                     }
#                 }
#             ]
#         }
#         active_dues: list = database_cuota.get_titles_rows_db(
#             filters=active_filter)
#         return jsonify({'month': active_dues, 'message': "Active Dues."})
#     except Exception as ex:
#         return jsonify({'message': f"Error: {ex}"})

@users.route('/login', methods=['POST'])
def login() -> dict:
    """Valida si el usuario existe en DB"""
    username = request.json['username']
    password = request.json['password']
    users_database = UsuarioAngular()

    page_user_data = users_database.login(username=username, password=password)
    if page_user_data:
        encoded_token = Security.generate_token(page_user_data)
        return jsonify({
            'exists': True,
            'token': encoded_token
            }
        )
    else:
        return jsonify({'exists': False}), 401

@users.route('/users/<username>')
def get_user(username: str) -> dict:
    """Obtiene la información de un usuario específica"""
    try:
        users_database = UsuarioAngular()

        page_user_data = users_database.get_user(username)
        if page_user_data:
            return jsonify({'user': page_user_data, 'message': "Usuario obtenido correctamente."})
        else:
            return jsonify({'message': "Usuario no encontrada."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})

@users.route('/users', methods=["POST"])
def add_user() -> dict:
    """
    Agrega un usuario a la base de datos.

    Returns:
        None. Retorna un mensaje JSON indicando el resultado de la operación.
    """
    try:
        users_database = UsuarioAngular()

        users_props_body: dict = {
            "Usuario": request.json["user"],
            "Email": request.json["email"],
            "Nombre Completo": request.json["fullname"], 
            "Contraseña": request.json["password"]
        }
        new_user_data: dict = users_database.create_page(props_modified=users_props_body)
        new_user_data_props = new_user_data["properties"]
        if new_user_data:
            return jsonify({'new_user': new_user_data,
                            'message': "Usuario creado correctamente."})
        else:
            return jsonify({'message': "Error al crear el usuario."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})
