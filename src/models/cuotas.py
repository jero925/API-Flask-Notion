"""Model para la base de datos cuotas"""
import os
from .database_model import SpecificDatabase
class Cuota(SpecificDatabase):
    """
    Inicializa una instancia de Cuota.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("CUOTAS_DB_ID")
        super().__init__(database_id=self.database_id)
        self.icon: str = "https://www.notion.so/icons/credit-card_gray.svg"
        self.properties: dict = {
            "Monto Total": {
                "number": 1
            },
            "Cantidad de cuotas": {
                "select": {
                    "name": "6"  # requerido
                }
            },
            "Monto Regalado": {
                "number": 0
            },
            "Primer cuota": {
                "date": {
                    "start": "2024-02-13"
                }
            },
            "Fecha de compra": {
                "date": {
                    "start": "2024-03-13"
                }
            },
            "Meses": {
                "type": "relation",
                "relation": []
            },
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "NombreDelRegistro"
                        }
                    }
                ]
            }
        }

def create_cuota_page(cuota: Cuota) -> None:
    """Ejemplo de creacion de pagina en DB Cuotas"""
    cuota_props_modified: dict = {
        "icon": "https://www.notion.so/icons/credit-card_gray.svg",
        "parent": "",
        "Name": "Prueba ejecucion de cosas",
        "Monto Total": 999999,
        "Cantidad de cuotas": "12",
        "Primer cuota": "2024-11-15",
        "Fecha de compra": "2024-07-29",
        "Meses": ["d9c435da42a445b48ceaf181a5615380",
                  "6479ae15-e5c1-46b6-bf8a-d41918bcb071",
                  "8c3a3aa1-5bb2-43a4-bb28-2f9e4e986feb"]
    }

    # cuota_props_dict: dict = cuota_props_modified.to_dict
    # print(cuota_props_modified)
    cuota.create_page(props_modified=cuota_props_modified)

def main() -> None:
    """
    Función principal para demostrar el uso de la clase Database.
    """
    cuota_database = Cuota()

    filtros: dict = {
        "and": [
            {
                "property": "Activa",
                "checkbox": {
                    "equals": True
                }
            }
        ]
    }

    create_cuota_page(cuota_database)

    # query_database_results = db.query_database(filters=filtros)
    # print(query_database_results)

    # names_rows_results: dict = db.get_titles_rows_db(filters=filtros)
    # print(names_rows_results)

if __name__ == "__main__":
    main()
