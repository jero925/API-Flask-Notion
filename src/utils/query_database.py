import os

from notion_client import Client

apiKeyNotion = os.getenv("NOTION_SECRET")

database_Id = os.getenv("CUOTAS_DB_ID")

notion = Client(auth=apiKeyNotion)

def query_database(database_id: str, filters=None) -> dict:
    """
    Consulta una base de datos con filtros opcionales.

    Args:
        database_id (str): El ID de la base de datos que se desea consultar.
        filters (dict, opcional): Filtros que se aplicarán a la consulta.

    Returns:
        list: Una lista de registros que coinciden con la consulta.
    """
    query_params = {"database_id": database_id}
    if filters is not None:
        query_params["filter"] = filters

    response = notion.databases.query(**query_params)
    results = response["results"]
    return results

if __name__ == "__main__":
    resultados = query_database(database_id=database_Id)
    print(resultados)
