from pprint import pprint
import os
from query_database import query_database

database_id = os.getenv("CUOTAS_DB_ID")

# from services.define_env_variables import dbCuotas

def get_names_rows_db(database_id: str, filters=None) -> list:
    """
    Recupera nombres de una base de datos.

    Args:
        database_id (str): El ID de la base de datos de la que se desean recuperar los nombres.
        filters (dict, opcional): Filtros que se aplicarán a la consulta.

    Returns:
        list: Una lista de nombres de los registros de base de datos especificada.
    """
    results = query_database(database_id)
    rows_name_list = [result["properties"]["Name"]["title"][0]["plain_text"] for result in results]
    return rows_name_list

if __name__ == "__main__":
    names_list = get_names_rows_db(database_id)
    print(names_list)
