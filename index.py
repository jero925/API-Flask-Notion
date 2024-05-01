"""archivo main"""
import define_env_variables as env
from src.services import databases
from src.database import db_properties, db_structures


cuota_props_dict = db_properties.cuota_props.to_dict()

databases.create_page(env.dbCuotas, db_structures.cuota, cuota_props_dict)
