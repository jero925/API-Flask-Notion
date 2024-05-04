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

    def __init__(self, database_id: str, name: str) -> None:
        self.database_id: str = database_id
        self.name: str = name
        self.properties = {}

    def query_database(self, database_id: str, filters: dict = None) -> dict:
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

    def get_titles_rows_db(self, filters: dict = None) -> dict:
        """
        Recupera los nombres de los registros de una base de datos.

        Args:
            database_id (str): El ID de la base de datos.
            filters (dict, opcional): Filtros aplicados a la consulta.

        Returns:
            list: Lista de nombres de los registros que coinciden con la consulta.
        """
        results: dict = self.query_database(self.database_id, filters)
        rows_titles = []
        for result in results:
            row_dict = {
                "id": result["id"],
                "nombre": result["properties"]["Name"]["title"][0]["plain_text"]
            }
            rows_titles.append(row_dict)

        return rows_titles

    def get_property_data_type(self, properties: dict, prop: str) -> list:
        """
        Obtiene el tipo de datos de una propiedad en una base de datos de Notion.

        Args:
            properties (dict): Las propiedades de la base de datos.
            prop (str): El nombre de la propiedad.

        Returns:
            str: El tipo de datos de la propiedad especificada.
        """
        data_type: list[str] = list(properties[prop].keys())[-1]

        return data_type

    def get_page_by_id(self, page_id: str) -> dict:
        """
        Obtiene una pagina determinada mediante su ID

        Args:
            page_id (str): Pagina y sus propiedades
        """
        database_entries = self.get_titles_rows_db()
        if any(page_id in entry["id"] for entry in database_entries):
            page_result = notion.pages.retrieve(page_id=page_id)

        return page_result

    def create_page(self, database_id: str, props_page: dict, props_modified: dict) -> dict:
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
        for modified_prop_key, modified_prop_value in props_modified.items():
            # print(f"esta entrando en: {modified_prop_key} valor: {modified_prop_key}")
            if modified_prop_key in props_page.keys():
                page_prop_value = modified_prop_key
                prop_data_type = self.get_property_data_type(
                    props_page, page_prop_value)
                # print(prop_data_type)
                # Actualiza las propiedades en función de sus tipos de datos
                match prop_data_type:
                    case "title":
                        props_page[page_prop_value]["title"][0]["text"]["content"] = (
                            modified_prop_value
                        )
                    case "number":
                        props_page[page_prop_value]["number"] = modified_prop_value
                    case "select":
                        props_page[page_prop_value]["select"]["name"] = modified_prop_value
                    case "date":
                        props_page[page_prop_value]["date"]["start"] = modified_prop_value
                    case "relation":
                        for relation in modified_prop_value:
                            props_page[page_prop_value]["relation"].append(
                                {"id": relation})
                    case "multi_select":
                        # print(f"modificada valor: {modified_prop_value}")
                        for select_name in modified_prop_value:
                            # print(select_name)
                            props_page[page_prop_value]["multi_select"].append(
                                {"name": select_name}
                            )

        # Construye las propiedades de la página, el padre y el ícono para crear la página
        page_properties: dict = props_page
        page_parent: dict = {"database_id": database_id}
        page_icon: dict = {"type": "external",
                           "external": {"url": props_modified["icon"]}}
        # Crea la página en Notion y devuelve la respuesta
        new_page = notion.pages.create(
            parent=page_parent,
            icon=page_icon,
            properties=page_properties)
        return new_page


class Cuota(Database):
    """
    Inicializa una instancia de Cuota.
    """

    def __init__(self) -> None:
        self.database_id: str = os.getenv("CUOTAS_DB_ID")
        super().__init__(database_id=self.database_id, name="Cuota")
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

    def create_page(self, props_modified: dict) -> dict:
        """
        Crea una nueva página en la base de datos con las propiedades modificadas.

        Args:
            props_modified (dict): Diccionario de propiedades modificadas.

        Returns:
            dict: Retorna un diccionario representando la página creada.
        """
        props_modified["icon"] = self.icon
        return super().create_page(
            database_id=self.database_id,
            props_page=self.properties,
            props_modified=props_modified
        )


def create_cuota_page(database: Database) -> None:
    """Ejemplo de creacion de pagina en DB Cuotas"""
    cuota_props: dict = {
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
    database.create_page(
        database_id=database.database_id,
        props_page=cuota_props,
        props_modified=cuota_props_modified)


def create_flujo_plata_page(database: Database):
    """Ejemplo de creacion de pagina en DB Flujo Plata"""
    flujo_plata_props = {
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
    flujo_plata_props_modified: dict = {
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

    # cuota_props_dict: dict = cuota_props_modified.to_dict
    # print(cuota_props_modified)
    database.create_page(
        database_id=database.database_id,
        props_page=flujo_plata_props,
        props_modified=flujo_plata_props_modified)


def main() -> None:
    """
    Función principal para demostrar el uso de la clase Database.
    """
    # database_id: str = os.getenv("FLUJOPLATA_DB_ID")
    database_id: str = os.getenv("CUOTAS_DB_ID")

    # Crear una instancia de la clase Database
    db: Database = Database(database_id=database_id, name="nombre")

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
    # query_database_results = db.query_database(filters=filtros)
    # print(query_database_results)

    names_rows_results: dict = db.get_titles_rows_db(filters=filtros)
    print(names_rows_results)

    # create_cuota_page(database=db)
    # create_flujo_plata_page(database=db)


if __name__ == "__main__":
    main()
