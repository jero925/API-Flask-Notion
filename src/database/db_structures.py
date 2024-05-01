"""Estructuras de las db para el cuerpo de la request"""
cuota = {
    "Monto Total": {
        "number": 1
    },
    "Cantidad de cuotas": {
        "select": {
            "name": "6" #requerido
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

flujo_plata = {
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
            "id": "HFQR",
            "type": "multi_select",
            "multi_select": [
                {
                    "name": "Comida"
                },
                {
                    "name": "Social"
                }
            ]
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
