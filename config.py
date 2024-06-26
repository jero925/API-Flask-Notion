"""Obtiene variables de entorno"""
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

apiKeyNotion = os.getenv("NOTION_SECRET")
dbCalendario = os.getenv("CALENDARIO_DB_ID")
dbMetPago = os.getenv("MET_PAGO_DB_ID")
dbMeses = os.getenv("MESES_DB_ID")
dbFlujoPlata = os.getenv("FLUJOPLATA_DB_ID")
dbCuotas = os.getenv("CUOTAS_DB_ID")

env_config = dotenv_values(".env")

if __name__ == "__main__":
    print(env_config)
