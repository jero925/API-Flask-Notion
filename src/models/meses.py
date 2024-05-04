"""Model para la base de datos cuotas"""
import os
from .database_model import SpecificDatabase
class Meses(SpecificDatabase):
    """
    Inicializa una instancia de Cuota.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("MESES_DB_ID")
        super().__init__(database_id=self.database_id)
        self.icon: str = ""
        self.properties: dict = {
            "Actual": {
                "formula": {
                    "boolean": True,
                    "type": "boolean"
                },
                "id": "%3DME%40",
                "type": "formula"
            },
            "Año": {
                "has_more": False,
                "id": "KpHO",
                "relation": [
                    {
                        "id": "f1d456cd-efcb-4ce1-a9cc-2ec1b5b3dc19"
                    }
                ],
                "type": "relation"
            },
            "Cover": {
                "files": [],
                "id": "lr%3BT",
                "type": "files"
            },
            "Cuotas": {
                "has_more": True,
                "id": "%3Di_Y",
                "relation": [],
                "type": "relation"
            },
            "Date": {
                "date": {
                    "end": "2024-05-31",
                    "start": "2024-05-01",
                },
                "id": "Dmry",
                "type": "date"
            },
            "Este año": {
                "formula": {
                    "boolean": True,
                    "type": "boolean"
                },
                "id": "VLUw",
                "type": "formula"
            },
            "Mes": {
                "id": "title",
                "title": [
                    {
                        "plain_text": "Mayo 2024",
                        "text": {
                            "content": "Mayo 2024",
                        },
                        "type": "text"
                    }
                ],
                "type": "title"
            },
            "Suscripciones": {
                "has_more": False,
                "id": "h~bt",
                "relation": [],
                "type": "relation"
            },
            "alBalance": {
                "has_more": False,
                "relation": [],
                "type": "relation"
            }
        }

    def get_actual_month(self) -> dict:
        """Obtiene el mes actual de la base de Datos 'Meses'

        Returns:
            dict: información del registro marcado como actual
        """
        filters: dict = {
            "and": [
                {
                    "property": "Actual",
                    "checkbox": {
                        "equals": True
                    }
                }
            ]
        }

        actual_month = super().get_titles_rows_db(filters=filters)
        return actual_month

def main():
    """Main function"""
    meses_database = Meses()

    filters: dict = {
        "and": [
            {
                "property": "Actual",
                "checkbox": {
                    "equals": True
                }
            }
        ]
    }

    meses_data = meses_database.query_specific_database(filters=filters)
    print(meses_data)

if __name__ == "__main__":
    main()
