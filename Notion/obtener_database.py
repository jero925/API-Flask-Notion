"""Obtiene una db específica"""
import valorizar_venv as env
from notion_client import Client

from db import db_properties, db_structures

# Inicializa el cliente de Notion
notion = Client(auth=env.apiKeyNotion)

def get_database(dbid: str) -> dict:
    """
    Recupera toda la información de una base de datos utilizando su ID.

    Args:
        dbid (str): El ID de la base de datos que se desea recuperar.

    Returns:
        dict: Un diccionario que contiene información sobre la base de datos especificada.
    """
    response = notion.databases.retrieve(database_id=dbid)
    return response

def query_database(dbid: str, filters=None) -> dict:
    """
    Consulta una base de datos con filtros opcionales.

    Args:
        dbid (str): El ID de la base de datos que se desea consultar.
        filters (dict, opcional): Filtros que se aplicarán a la consulta.

    Returns:
        list: Una lista de registros que coinciden con la consulta.
    """
    query_params = {"database_id": dbid}
    if filters is not None:
        query_params["filter"] = filters

    response = notion.databases.query(**query_params)
    results = response["results"]
    return results

def get_names_db(dbid: str, filters=None) -> list:
    """
    Recupera nombres de una base de datos.

    Args:
        dbid (str): El ID de la base de datos de la que se desean recuperar los nombres.
        filters (dict, opcional): Filtros que se aplicarán a la consulta.

    Returns:
        list: Una lista de nombres de la base de datos especificada.
    """
    results = query_database(dbid, filters)
    nombres = [result["properties"]["Name"]["title"][0]["plain_text"] for result in results]
    return nombres

def get_property_data_type(properties: dict, prop: str) -> list:
    """
    Obtiene el tipo de datos de una propiedad en una base de datos de Notion.

    Args:
        properties (dict): Las propiedades de la base de datos.
        prop (str): El nombre de la propiedad.

    Returns:
        str: El tipo de datos de la propiedad especificada.
    """
    data_type = list(properties[prop].keys())[0]
    return data_type

def create_page(database_id: str, props_page=None, props_modified=None) -> dict:
    """
    Crea una nueva página en una base de datos de Notion con propiedades modificadas.

    Args:
        database_id (str): El ID de la base de datos en la que se creará la página.
        props_page (dict): Las propiedades originales de la página.
        props_modified (dict): Las propiedades modificadas de la página.

    Returns:
        dict: Información sobre la página recién creada.
    """

    # Verifica si se proporcionan las propiedades de la página
    if props_page is None:
        print("Error: No se proporcionaron las propiedades de la página.")
        return

    # Actualiza las propiedades de la página según las modificaciones especificadas
    for mod_key, mod_value in props_modified.items():
        if mod_key in props_page.keys():
            page_key = mod_key
            prop_data_type = get_property_data_type(props_page, page_key)

            # Actualiza las propiedades en función de sus tipos de datos
            match prop_data_type:
                case "title":
                    props_page["Name"]["title"][0]["text"]["content"] = mod_value
                case "number":
                    props_page[page_key]["number"] = mod_value
                case "select":
                    props_page[page_key]["select"]["name"] = mod_value
                case "date":
                    props_page[page_key]["date"]["start"] = mod_value

    # Construye las propiedades de la página, el padre y el ícono para crear la página
    page_properties = props_page
    page_parent = {"database_id": database_id}
    page_icon = {"type": "external", "external": {"url": props_modified["icon"]}}

    # Crea la página en Notion y devuelve la respuesta
    new_page = notion.pages.create(parent=page_parent, icon=page_icon, properties=page_properties)
    print(new_page)
    # return new_page

create_page(env.dbCuotas, db_structures.cuota_db, db_properties.cuota_props)
