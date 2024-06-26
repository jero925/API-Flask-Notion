"""Definición de rutas para lógica de movimientos"""
from flask import Blueprint, jsonify
from ..models.books import Bookcase
from ..models.genres import Genres

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
    try:
        genres_database = Genres()

        select_properties = genres_database.get_titles_rows_db()
        # books_data_json = books_database.to_json(select_properties)
        if select_properties:
            return jsonify(select_properties)
        else:
            return jsonify({'message': "No se han encontrado libros."})
    except Exception as ex:
        return jsonify({'message': f"Error: {ex}"})
