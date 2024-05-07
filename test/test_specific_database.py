"""
    Testeos de los métodos de la clase Database.
    Se utiliza a modo de ejemplo la Base de Datos "Flujo Plata"
"""
import os
import pytest
from ..src.models.database_model import SpecificDatabase

@pytest.fixture
def specific_database_instance() -> SpecificDatabase:
    """
    Fixture para crear una instancia de Database para las pruebas.

    Returns:
        Database: Una instancia de la clase Database configurada para las pruebas.
    """
    # Obtiene el ID de la base de datos desde la variable de entorno
    database_id: str = os.getenv("FLUJOPLATA_DB_ID")

    # Crea una instancia de Database
    specific_database: SpecificDatabase = SpecificDatabase(database_id=database_id)

    # Define las propiedades de ejemplo para la base de datos
    specific_database.properties = {
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

    return specific_database

def test_get_rows_titles(specific_database_instance: SpecificDatabase):
    """
    Prueba la función get_titles_rows_db de la clase Database.

    Args:
        specific_database_instance (SpecificDatabase): Instancia de SpecificDatabase para la prueba.
    """
    filters = {"property": "Nombre", "rich_text": {"contains": "Monotributo"}}
    # Obtiene los nombres de los registros
    rows_titles: dict = specific_database_instance.get_titles_rows_db()
    # Verifica que haya al menos un registro
    assert len(rows_titles) > 0

def test_query_database(specific_database_instance: SpecificDatabase):
    filters: dict = {"property": "Nombre", "rich_text": {"contains": "Testing Execution"}}

    query_results: dict = specific_database_instance.query_database(filters=filters)
    assert query_results is not None

def test_database_title_property(specific_database_instance: SpecificDatabase):
    """
    Prueba la función get_database_title_property de la clase Database.

    Args:
        specific_database_instance (Database): Instancia de Database para la prueba.
    """
    # Obtiene el nombre de la propiedad que es un título
    database_title_prop: str = specific_database_instance.get_database_title_property()
    # Verifica que la propiedad de título sea la esperada
    assert database_title_prop == "Nombre"

def test_property_data_type(specific_database_instance: SpecificDatabase):
    """
    Prueba la función get_property_data_type de la clase Database.

    Args:
        specific_database_instance (Database): Instancia de Database para la prueba.
    """
    # Obtiene el tipo de datos de la propiedad de título
    title_property: str = specific_database_instance.get_database_title_property()
    data_type_result: str = specific_database_instance.get_property_data_type(
        specific_database_instance.properties,
        title_property
    )
    # Verifica que el tipo de datos sea el esperado
    assert data_type_result == "title"

def test_create_page(specific_database_instance: SpecificDatabase):
    """
    Prueba la función create_page de la clase Database.

    Args:
        specific_database_instance (Database): Instancia de Database para la prueba.
    """
    # Define las propiedades modificadas para la nueva página
    modified_properties: dict = {
        "icon": "https://www.notion.so/icons/credit-card_gray.svg",
        "parent": "",
        "Nombre": "Testing Execution",
        "Monto": 123456,
        "I/O": "Gasto",
        "Fecha": "2024-11-15",
        "Cuenta": [],
        "Gasto. Mes Año": ["d9c435da42a445b48ceaf181a5615380"],
        "Tipo": ["Sueldo", "Suscripcion"]
    }

    # Crea una nueva página
    new_page = specific_database_instance.create_page(props_modified=modified_properties)

    # Verifica que la página se haya creado correctamente
    assert new_page is not None

def test_delete_page(specific_database_instance: SpecificDatabase):
    """
    Prueba la función delete_page_by_id de la clase Database.

    Args:
        specific_database_instance (Database): Instancia de Database para la prueba.
    """
    filters: dict = {"property": "Nombre", "rich_text": {"contains": "Testing Execution"}}
    # Busca una página creada para la prueba
    test_created_page: dict = specific_database_instance.get_titles_rows_db(filters=filters)

    # Si se encontró una página, intenta eliminarla
    if test_created_page is not None:
        deleted_page_results = specific_database_instance.delete_page_by_id(
            test_created_page[0]["id"])

    # Verifica que la página se haya eliminado correctamente
    assert deleted_page_results is not None
