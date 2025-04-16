from datetime import datetime
from model.food import Food

class DailyConsumption:
    def __init__(self, food, quantity_grams, date=None):
        if not isinstance(food, Food):
            raise TypeError("food deve ser uma instância da classe Food.")
        if quantity_grams <= 0:
            raise ValueError("A quantidade consumida deve ser maior que zero.")
        
        self.food = food  # Alimento consumido
        self.quantity_grams = quantity_grams  # Quantidade consumida
        self.date = date if date else datetime.now().date().isoformat()  # Data do consumo

    def to_dict(self):
        return {
            "food": self.food.to_dict(),
            "quantity_grams": self.quantity_grams,
            "date": self.date
        }
