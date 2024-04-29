"""Estructuras de las db"""
cuota_db = {
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
