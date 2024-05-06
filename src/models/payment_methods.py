"""Model para la base de datos cuotas"""
import os
from .database_model import SpecificDatabase
class MetodoPago(SpecificDatabase):
    """
    Inicializa una instancia de Cuentas.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("MET_PAGO_DB_ID")
        super().__init__(database_id=self.database_id)
        self.icon: str = "https://www.notion.so/icons/library_gray.svg"
        self.properties: dict = {
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

def main() -> None:
    """
    Función principal para demostrar el uso de la clase Database.
    """
    db_payment_methods = MetodoPago()

    payment_method_props_modified: dict = {
        "icon": "",
        "Name": "Test file"
    }

    db_payment_methods.create_page(props_modified=payment_method_props_modified)

    filters: dict = {"property": "Name", "rich_text": {"contains": "Macro"}}

    # query_database_results = db_payment_methods.query_database(filters=filtros)
    # print(query_database_results)

    names_rows_results: dict = db_payment_methods.get_titles_rows_db()
    print(names_rows_results)

if __name__ == "__main__":
    main()
