"""asdasds"""
class Cuota():
    """Corresponde a los datos de la DB Cuotas"""
    def __init__(self, parent, name, total_price, dues_qty, date_first_due, buy_due, months) -> None:
        self.icon = "https://www.notion.so/icons/credit-card_gray.svg"
        self.parent = parent
        self.name = name
        self.total_price = total_price
        self.dues_qty = dues_qty
        self.date_first_due = date_first_due
        self.buy_due = buy_due
        self.months = months

    def to_dict(self):
        """Transforma clase a dict"""
        return {
            "icon": self.icon,
            "parent": self.parent,
            "Name": self.name,
            "Monto Total": self.total_price,
            "Cantidad de cuotas": self.dues_qty,
            "Primer cuota": self.date_first_due,
            "Fecha de compra": self.buy_due,
            "Meses": self.months
        }
