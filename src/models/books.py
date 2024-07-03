"""Model para la base de datos UsuariosAngular"""
import os
from .database_model import SpecificDatabase


class Bookcase(SpecificDatabase):
    """
    Inicializa una instancia de Bookcase.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("BOOKCASE_DB_ID")
        super().__init__(database_id=self.database_id)
        self.properties: dict = {
            "Author": {
                "id": "%3AMeY",
                "type": "multi_select",
                "multi_select": []
            },
            "Total pags": {
                "id": "%3B%3Am~",
                "type": "number",
                "number": 1
            },
            "Estado": {
                "id": "%3FjJr",
                "type": "select",
                "select": {
                    "name": "",
                }
            },
            "ISBN_10": {
                "id": "%40%3AVN",
                "type": "rich_text",
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": ""
                        }
                    }
                ]
            },
            "Año Leido": {
                "id": "AmtG",
                "type": "relation",
                "relation": [],
            },
            "Start and End": {
                "id": "BPoT",
                "type": "date",
                "date": {
                    "start": "2024-06-25",
                    "end": None
                }
            },
            "Fisico": {
                "id": "Bhc%3F",
                "type": "checkbox",
                "checkbox": False
            },
            "Puntaje": {
                "id": "VRm%7C",
                "type": "select",
                "select": {
                    "name": "",
                }
            },
            "Type": {
                "id": "%60p%3Eo",
                "type": "select",
                "select": {
                    "name": "Book"
                }
            },
            "Genre": {
                "id": "fKM%5B",
                "type": "relation",
                "relation": []
            },
            "Leidas": {
                "id": "hOrn",
                "type": "number",
                "number": None
            },
            "Coleccion Terminada": {
                "id": "t%5BKB",
                "type": "checkbox",
                "checkbox": False
            },
            "ISBN_13": {
                "id": "y%7BNN",
                "type": "rich_text",
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": ""
                        }
                    }
                ]
            },
            "Name": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": ""
                        }
                    }
                ]
            }
        }

    def get_book_by_isbn_10(self, isbn: str) -> dict:
        """Obtiene el un usuario específico

        Returns:
            dict: información del registro
        """
        filters: dict = {
            "and": [
                {
                    "property": "ISBN_10",
                    "rich_text": {
                        "equals": isbn
                    }
                }
            ]
        }

        book_data = super().query_database(filters=filters)
        book_json = super().to_json(book_data)
        return book_json

    def get_book_by_isbn_13(self, isbn: str) -> dict:
        """Obtiene el un usuario específico

        Returns:
            dict: información del registro
        """
        filters: dict = {
            "and": [
                {
                    "property": "ISBN_13",
                    "rich_text": {
                        "equals": isbn
                    }
                }
            ]
        }

        book_data = super().query_database(filters=filters)
        book_json = super().to_json(book_data)
        return book_json

def create_db_page(bookcase: Bookcase) -> None:
    """Ejemplo de creacion de pagina en DB Cuotas"""
    database_props_modified: dict = {
        "cover": "http://books.google.com/books/content?id=hWSmEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api", 
        "icon": "http://books.google.com/books/content?id=hWSmEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
        "parent": "",
        "Name": "Pepito",
        "Author": ["Brandon Sanderson"],
        "Total pags": 320,
        "Estado": "Reading",
        "ISBN_13": "123123",
        "Año Leido": ["f1d456cd-efcb-4ce1-a9cc-2ec1b5b3dc19"],
        "Start and End": "2024-11-15",
        "Puntaje": "⭐⭐⭐",
        "Genre": ["36bb79c6-3b11-40ef-bf3f-c3f6a27568a0"],
    }
    # print(database_props_modified)
    bookcase.create_page(props_modified=database_props_modified)

if __name__ == "__main__":
    bookcase_database = Bookcase()
    create_db_page(bookcase_database)
