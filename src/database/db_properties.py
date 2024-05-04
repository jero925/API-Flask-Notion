"""Crea el diccionario para DB Cuotas"""
from ..models.cuota_model import Cuota

cuota_props = Cuota(
    parent = "",
    name = "Prueba ejecucion de cosas",
    total_price = 999999,
    dues_qty = "12",
    date_first_due = "2024-11-15",
    buy_due = "2024-07-29",
    months = ["d9c435da42a445b48ceaf181a5615380",
              "6479ae15-e5c1-46b6-bf8a-d41918bcb071",
              "8c3a3aa1-5bb2-43a4-bb28-2f9e4e986feb"]
)
