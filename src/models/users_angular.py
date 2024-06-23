"""Model para la base de datos UsuariosAngular"""
import os
from .database_model import SpecificDatabase


class UsuarioAngular(SpecificDatabase):
    """
    Inicializa una instancia de UsuariosAngular.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("USUARIOS_DB_ID")
        super().__init__(database_id=self.database_id)
        self.properties: dict = {
            "Nombre Completo": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "",
                        }
                    }
                ]
            },
            "Email": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "",
                        }
                    }
                ]
            },
            "Contraseña": {
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
            "Usuario": {
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

    def get_user(self, username: str) -> dict:
        """Obtiene el un usuario específico

        Returns:
            dict: información del registro
        """
        filters: dict = {
            "and": [
                {
                    "property": "Usuario",
                    "rich_text": {
                        "equals": username
                    }
                }
            ]
        }

        user_data = super().query_database(filters=filters)
        user_json = super().to_json(user_data)
        return user_json

    def login(self, username: str, password: str) -> dict:
        """Obtiene el un usuario específico

        Returns:
            dict: información del registro
        """
        filters: dict = {
            "and": [
                {
                    "property": "Usuario",
                    "rich_text": {
                        "equals": username
                    }
                },
                {
                    "property": "Contraseña",
                    "rich_text": {
                        "equals": password
                    }
                }
            ]
        }

        user_data = super().query_database(filters=filters)
        return user_data
 