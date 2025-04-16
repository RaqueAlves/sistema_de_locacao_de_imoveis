class Food:
    def __init__(self, name, quantity_grams, calories_per_serving, protein, carbohydrates, fat):
        self._name = None  
        self._quantity_grams = None  
        self._calories_per_serving = None  
        self._protein = None  
        self._carbohydrates = None  
        self._fat = None 

        self._name = name  
        self._quantity_grams = quantity_grams  
        self._calories_per_serving = calories_per_serving 
        self._protein = protein  
        self._carbohydrates = carbohydrates  
        self._fat = fat 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("O atributo deve ser uma string com mais de 3 caracteres.")

    @property
    def quantity_grams(self):
        return self._quantity_grams

    @quantity_grams.setter
    def quantity_grams(self, quantity_grams):
        if quantity_grams > 0:
            self._quantity_grams = quantity_grams
        else:
            raise ValueError("Quantity must be greater than 0")
        
    @property    
    def calories_per_serving(self):
        return self._calories_per_serving

    @calories_per_serving.setter
    def calories_per_serving(self, calories_per_serving):
        if calories_per_serving >= 0:
            self._calories_per_serving = calories_per_serving
        else:
            raise ValueError("Calories must be non-negative")
        
    @property
    def protein(self):
        return self._protein

    @protein.setter
    def protein(self, protein):
        if protein >= 0:
            self._protein = protein
        else:
            raise ValueError("Protein must be non-negative")
        
    @property
    def carbohydrates(self):
        return self._carbohydrates

    @carbohydrates.setter
    def carbohydrates(self, carbohydrates):
        if carbohydrates >= 0:
            self._carbohydrates = carbohydrates
        else:
            raise ValueError("Carbohydrates must be non-negative")

    @property
    def fat(self):
        return self._fat

    @fat.setter
    def fat(self, fat):
        if fat >= 0:
            self._fat = fat
        else:
            raise ValueError("Fat must be non-negative")
        
    @property
    def caloric_density(self):
        """retorna a densidade calórica em kcal por grama do alimento"""
        if self.quantity_grams > 0:
            return self.calories_per_serving / self.quantity_grams
        return 0
        
    @property
    def protein_density(self):
        """retorna a densidade proteica em kcal por grama do alimento"""
        if self.quantity_grams > 0:
            return self.protein / self.quantity_grams
        return 0
    
    @property
    def carbohydrates_density(self):
        """retorna a densidade de carboidratos em kcal por grama do alimento"""
        if self.quantity_grams > 0:
            return self.carbohydrates / self.quantity_grams
        return 0
    
    @property
    def fat_density(self):
        """retorna a densidade de gordura em kcal por grama do alimento"""
        if self.quantity_grams > 0:
            return self.fat / self.quantity_grams
        return 0

    def to_dict(self):
        return {
            "name": self.name,
            "quantity_grams": self.quantity_grams,
            "calories_per_serving": self.calories_per_serving,
            "protein": self.protein,
            "carbohydrates": self.carbohydrates,
            "fat": self.fat
        }
    
    def __str__(self):
        return f"{self.name} ({self.quantity_grams}g)\n{self.calories_per_serving} kcal\nCaloric Density: {self.caloric_density}\nProtein: {self.protein}\nCarbohydrates: {self.carbohydrates}\nFat: {self.fat}"
