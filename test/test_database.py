"""
    Testeos de los métodos de la clase Database.
    Se utiliza a modo de ejemplo la Base de Datos "Cuota"
"""
import os
import pytest
from ..src.models.database_model import Database

@pytest.fixture
def database_instance() -> Database:
    """
    Fixture para crear una instancia de Database para las pruebas.

    Returns:
        Database: Una instancia de la clase Database configurada para las pruebas.
    """
    # Obtiene el ID de la base de datos desde la variable de entorno
    database_id: str = os.getenv("CUOTAS_DB_ID")

    # Crea una instancia de Database
    database: Database = Database(database_id=database_id)

    # Define las propiedades de ejemplo para la base de datos
    database.properties = {
        "Monto Total": {"number": 1},
        "Cantidad de cuotas": {"select": {"name": "6"}},
        "Monto Regalado": {"number": 0},
        "Primer cuota": {"date": {"start": "2024-02-13"}},
        "Fecha de compra": {"date": {"start": "2024-03-13"}},
        "Meses": {"type": "relation", "relation": []},
        "Name": {"title": [{"text": {"content": "NombreDelRegistro"}}]}
    }

    return database

def test_get_rows_titles(database_instance: Database):
    """
    Prueba la función get_titles_rows_db de la clase Database.

    Args:
        database_instance (Database): Instancia de Database para la prueba.
    """
    # Obtiene los nombres de los registros
    rows_titles: dict = database_instance.get_titles_rows_db()
    # Verifica que haya al menos un registro
    assert len(rows_titles) > 0

def test_database_title_property(database_instance: Database):
    """
    Prueba la función get_database_title_property de la clase Database.

    Args:
        database_instance (Database): Instancia de Database para la prueba.
    """
    # Obtiene el nombre de la propiedad que es un título
    database_title_prop: str = database_instance.get_database_title_property()
    # Verifica que la propiedad de título sea la esperada
    assert database_title_prop == "Name"

def test_property_data_type(database_instance: Database):
    """
    Prueba la función get_property_data_type de la clase Database.

    Args:
        database_instance (Database): Instancia de Database para la prueba.
    """
    # Obtiene el tipo de datos de la propiedad de título
    title_property: str = database_instance.get_database_title_property()
    data_type_result: str = database_instance.get_property_data_type(
        database_instance.properties,
        title_property
    )
    # Verifica que el tipo de datos sea el esperado
    assert data_type_result == "title"

def test_create_page(database_instance: Database):
    """
    Prueba la función create_page de la clase Database.

    Args:
        database_instance (Database): Instancia de Database para la prueba.
    """
    # Define las propiedades modificadas para la nueva página
    modified_properties: dict = {
        "icon": "https://www.notion.so/icons/credit-card_gray.svg",
        "parent": "",
        "Name": "Testing Execution",
        "Monto Total": 999999,
        "Cantidad de cuotas": "12",
        "Primer cuota": "2024-11-15",
        "Fecha de compra": "2024-07-29",
        "Meses": ["d9c435da42a445b48ceaf181a5615380",
                  "6479ae15-e5c1-46b6-bf8a-d41918bcb071",
                  "8c3a3aa1-5bb2-43a4-bb28-2f9e4e986feb"]
    }

    # Crea una nueva página
    new_page = database_instance.create_page(
        database_id=database_instance.database_id,
        props_page=database_instance.properties,
        props_modified=modified_properties)

    # Verifica que la página se haya creado correctamente
    assert new_page is not None

def test_delete_page(database_instance: Database):
    """
    Prueba la función delete_page_by_id de la clase Database.

    Args:
        database_instance (Database): Instancia de Database para la prueba.
    """
    # Busca una página creada para la prueba
    test_created_page: dict = database_instance.get_titles_rows_db(
        filters={"property": "Name", "rich_text": {"contains": "Testing Execution"}}
    )

    # Si se encontró una página, intenta eliminarla
    if test_created_page is not None:
        deleted_page_results = database_instance.delete_page_by_id(test_created_page[0]["id"])

    # Verifica que la página se haya eliminado correctamente
    assert deleted_page_results is not None
