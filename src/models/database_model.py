"""
    La idea es la siguiente: tener una class padre Databases, donde voy a crear una nueva
    class hija por cada DB que haya.
    En la padre, va a estar como metodos los comunes, get, create, etc.
    Los atributos icon, parent, name. El resto de atributos van a ser propios de cada class hija
"""
import os

from notion_client import Client

apiKeyNotion = os.getenv("NOTION_SECRET")
notion = Client(auth=apiKeyNotion)

# Crear una instancia de la clase Database
cuotas_database_id: str = os.getenv("CUOTAS_DB_ID")

class Database():
    """
    Clase base para interactuar con bases de datos en Notion.

    Attributes:
        database_id (str): El ID de la base de datos.
        name (str): El nombre de la base de datos.
    """

    def __init__(self, database_id: str, name: str) -> None :
        self.database_id: str = database_id
        self.name: str = name

    def query_database(self, database_id: str, filters: dict=None) -> dict:
        """
        Consulta una base de datos en Notion.

        Args:
            database_id (str): El ID de la base de datos.
            filters (dict, opcional): Filtros aplicados a la consulta.

        Returns:
            list: Lista de registros que coinciden con la consulta.
        """

        query_params: dict = {"database_id": database_id}
        if filters is not None:
            query_params["filter"] = filters

        response: dict = notion.databases.query(**query_params)
        results: dict = response["results"]
        return results

    def get_names_rows_db(self, database_id: str, filters: dict=None) -> list:
        """
        Recupera los nombres de los registros de una base de datos.

        Args:
            database_id (str): El ID de la base de datos.
            filters (dict, opcional): Filtros aplicados a la consulta.

        Returns:
            list: Lista de nombres de los registros que coinciden con la consulta.
        """
        results: dict = self.query_database(database_id, filters)
        rows_name_list: list = [result["properties"]["Name"]["title"][0]["plain_text"] for result in results]
        return rows_name_list

def main() -> None:
    """
    Función principal para demostrar el uso de la clase Database.
    """
    database_id: str = os.getenv("CUOTAS_DB_ID")

    # Crear una instancia de la clase Database
    db: Database = Database(database_id=database_id, name="nombre")

    # Crear los filtros como un diccionario Python
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
    # query_database_results = db.query_database(database_id=database_id, filters=filtros)
    # print(query_database_results)

    names_rows_results: list = db.get_names_rows_db(database_id=database_id, filters=filtros)
    print(names_rows_results)

if __name__ == "__main__":
    main()
