"""Model para la base de datos Flujo_Plata"""
import os
from .database_model import SpecificDatabase
class FlujoPlata(SpecificDatabase):
    """
    Inicializa una instancia de Cuota.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("FLUJOPLATA_DB_ID")
        super().__init__(database_id=self.database_id)
        self.icon: str = ""
        self.properties: dict = {
            "Fecha": {
                "type": "date",
                "date": {
                        "start": "2024-01-04"
                }
            },
            "Producto en cuotas": {
                "type": "relation",
                "relation": [],
            },
            "Cuenta": {
                "type": "relation",
                "relation": [],
            },
            "Tipo": {
                "type": "multi_select",
                "multi_select": []
            },
            "Suscripcion": {
                "type": "relation",
                "relation": [],
            },
            "I/O": {
                "type": "select",
                "select": {
                        "name": "Gasto"
                }
            },
            "Estado Suscripcion": {
                "type": "status",
                "status": {
                        "name": "No sub"
                }
            },
            "Ingreso. Mes Año": {
                "type": "relation",
                "relation": [],
            },
            "Monto": {
                "type": "number",
                "number": 1
            },
            "Gasto. Mes Año": {
                "type": "relation",
                "relation": [],
            },
            "Nombre": {
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

def create_db_page(flujo_plata: FlujoPlata) -> None:
    """Ejemplo de creacion de pagina en DB Cuotas"""
    database_props_modified: dict = {
        "icon": "https://www.notion.so/icons/credit-card_gray.svg",
        "parent": "",
        "Nombre": "Prueba flujo plata",
        "Monto": 123456,
        "I/O": "Gasto",
        "Fecha": "2024-11-15",
        "Cuenta": [],
        "Gasto. Mes Año": ["d9c435da42a445b48ceaf181a5615380"],
        "Tipo": ["Sueldo", "Suscripcion"]
    }

    # print(database_props_modified)
    flujo_plata.create_page(props_modified=database_props_modified)

def main() -> None:
    """
    Función principal para demostrar el uso de la clase Database.
    """
    flujo_plata_database = FlujoPlata()

    filtros: dict = {"property": "Activa","checkbox": {"equals": True}}

    create_db_page(flujo_plata_database)

    # query_database_results = flujo_plata_database.query_database()
    # print(query_database_results)

    # names_rows_results: dict = flujo_plata_database.get_titles_rows_db()
    # print(names_rows_results)

if __name__ == "__main__":
    main()
