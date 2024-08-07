"""Definición de rutas para lógica de movimientos"""
from flask import Blueprint, jsonify, request
from ..models.books import Bookcase
from ..models.genres import Genres
from src.utils.security import Security

books = Blueprint('books', __name__)


@books.route('/books')
def get_books() -> dict:
    """Obtiene todos los libros de la DB"""
    try:
        books_database = Bookcase()

        books_data = books_database.query_database()
        books_data_json = books_database.to_json(books_data)
        if books_data_json:
            return jsonify({'books': books_data_json})
        else:
            return jsonify({'message': "No se han encontrado libros."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@books.route('/books/<isbn13>')
def get_book_by_isbn13(isbn13: int) -> dict:
    """Obtiene todos los libros de la DB"""
    try:
        books_database = Bookcase()
        filters: dict = {
            "and": [
                {
                    "property": "ISBN_13",
                    "rich_text": {
                        "equals": isbn13
                    }
                }
            ]
        }

        books_data = books_database.query_database(filters=filters)
        books_data_json = books_database.to_json(books_data)
        if books_data_json:
            return books_data_json
        else:
            return jsonify({'message': "No se han encontrado libros."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@books.route('/books/retrieve')
def get_select_props() -> dict:
    """Obtiene todos los libros de la DB"""
    try:
        books_database = Bookcase()

        select_properties = books_database.extract_select_properties_info()
        # books_data_json = books_database.to_json(select_properties)
        if select_properties:
            return jsonify(select_properties)
        else:
            return jsonify({'message': "No se han encontrado libros."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@books.route('/books/genres')
def get_books_genre() -> dict:
    has_access = Security.verify_token(request.headers)

    if not has_access:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

    try:
        genres_database = Genres()

        select_properties = genres_database.get_titles_rows_db()
        if select_properties:
            return jsonify(select_properties)
        else:
            return jsonify({'message': "No se han encontrado libros."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})


@books.route('/books', methods=["POST"])
def create_book() -> dict:
    try:
        books_database = Bookcase()

        book_props_body: dict = {
            "icon": request.json["icon"],
            "cover": request.json["cover"],
            "parent": request.json["parent"],
            "Name": request.json["name"],
            "Author": request.json["author"],
            "Total pags": request.json["pages"],
            "Estado": request.json["status"],
            "ISBN_13": request.json["isbn_13"],
            "Año Leido": request.json["year"],
            "Start and End": request.json["start_end"],
            "Puntaje": request.json.get("score", ""),
            "Genre": request.json["genre"]
        }

        if book_props_body["Puntaje"] == "":
            del books_database.properties["Puntaje"]

        books_database.create_page(props_modified=book_props_body)
        return jsonify({'message': "Nuevo libro agregado."})
    except Exception as ex:
        return jsonify({'message': f"Error al crear nuevo libro: \n {ex}"}), 400

@books.route('/books/<page_id>', methods=["PATCH"])
def update_book(page_id) -> dict:
    try:
        books_database = Bookcase()

        book_props_body: dict = {
            # "parent": request.json["parent"],
            "Estado": request.json["status"],
            "Start and End": request.json["start_end"],
            "Puntaje": request.json.get("score", ""),
            "Genre": request.json["genre"]
        }

        if book_props_body["Puntaje"] == "":
            del books_database.properties["Puntaje"]

        books_database.update_page(page_id=page_id, props_modified=book_props_body)
        return jsonify({'message': "Libro actualizado."})
    except Exception as ex:
        return jsonify({'message': f"Error al actualizar el libro: {ex}"}), 400

@books.route('/books/<page_id>', methods=["DELETE"])
def delete_book(page_id) -> dict:
    try:
        books_database = Bookcase()

        books_database.delete_page(page_id=page_id)
        return jsonify({'message': "Libro eliminado correctamente."})
    except Exception as ex:
        return jsonify({'message': f"Error al eliminar el libro: {ex}"}), 400