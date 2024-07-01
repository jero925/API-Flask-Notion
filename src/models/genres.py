"""Model para la base de datos UsuariosAngular"""
import os
from .database_model import SpecificDatabase


class Genres(SpecificDatabase):
    """
    Inicializa una instancia de Bookcase.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("GENRES_DB_ID")
        super().__init__(database_id=self.database_id)
        self.properties: dict = {
            "Name": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "",
                        }
                    }
                ]
            }
        }
