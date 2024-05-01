"""Obtiene una db específica"""
import os

from notion_client import Client

apiKeyNotion = os.getenv("NOTION_SECRET")
# Inicializa el cliente de Notion
notion = Client(auth=apiKeyNotion)

def get_database(database_id: str) -> dict:
    """
    Recupera toda la información de una base de datos utilizando su ID.

    Args:
        database_id (str): El ID de la base de datos que se desea recuperar.

    Returns:
        dict: Un diccionario que contiene información sobre la base de datos especificada.
    """
    response = notion.databases.retrieve(database_id=database_id)
    return response

def get_property_data_type(properties: dict, prop: str) -> list:
    """
    Obtiene el tipo de datos de una propiedad en una base de datos de Notion.

    Args:
        properties (dict): Las propiedades de la base de datos.
        prop (str): El nombre de la propiedad.

    Returns:
        str: El tipo de datos de la propiedad especificada.
    """
    data_type = list(properties[prop].keys())[-1]
    return data_type

def create_page(database_id: str, props_page: dict, props_modified: dict) -> dict:
    """
    Crea una nueva página en una base de datos de Notion con propiedades modificadas.

    Args:
        database_id (str): El ID de la base de datos en la que se creará la página.
        props_page (dict): Las propiedades originales de la página.
        props_modified (dict): Las propiedades modificadas de la página.

    Returns:
        dict: Información sobre la página recién creada.
    """

    # print(props_page)

    # Actualiza las propiedades de la página según las modificaciones especificadas
    for mod_key, mod_value in props_modified.items():
        # print("esta entrando en: " + mod_key + " valor: " + mod_key)
        if mod_key in props_page.keys():
            page_key = mod_key
            prop_data_type = get_property_data_type(props_page, page_key)
            # print(prop_data_type)
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
                case "relation":
                    for relation in mod_value:
                        props_page[page_key]["relation"].append({"id": relation})

    # Construye las propiedades de la página, el padre y el ícono para crear la página
    page_properties = props_page
    page_parent = {"database_id": database_id}
    page_icon = {"type": "external", "external": {"url": props_modified["icon"]}}
    # print(props_page)
    # Crea la página en Notion y devuelve la respuesta
    new_page = notion.pages.create(parent=page_parent, icon=page_icon, properties=page_properties)
    print(new_page)
    return new_page
