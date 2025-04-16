from model.daily_consumption import DailyConsumption

class User:
    def __init__(self, name, age, gender, weight, height, activity_level=None, goals=None):
        self._name = None
        self._age = None
        self._gender = None
        self._weight = None
        self._height = None
        self._activity_level = activity_level if activity_level is not None else ""
        self._goals = goals if goals is not None else ""
        self._daily_consumption = []  # Lista de alimentos consumidos

        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 3:
            self._name = name
        else:
            raise ValueError("O nome deve conter mais de 3 caracteres.")

    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age >= 18:
            self._age = age
        else:
            raise ValueError("Usuário deve ser maior de idade") 
        
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, gender):
        valid_genders = ["Feminino", "Masculino"]

        if gender in valid_genders:
            self._gender = gender
        else:
            raise ValueError("Gênero fornecido não é valido.")

    @property
    def weight(self):
        return self._weight
        
    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (float, int)) and weight > 0:
            self._weight = weight
        else:
            raise ValueError("Peso deve ser um valor positivo.")
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if isinstance(height, (float, int)) and height > 0:
            self._height = height
        else:
            raise ValueError("Altura deve ser um valor positivo.")
        
    def add_goals(self, goal):
        goal_lower = goal.lower()
        valid_goals = ["perda de peso", "manutenção", "ganho de massa"]
        
        if goal_lower in valid_goals:
            self._goals = goal_lower
        else:
            raise ValueError("Valor inválido!")

    @property
    def goals(self):
        return self._goals
    
    def add_activity_level(self, level):
        level_lower = level.lower()
        valid_levels = ["sedentário", 
                        "atividade leve", 
                        "atividade moderada", 
                        "atividade intensa", 
                        "atividade muito intensa"]
        
        if level_lower in valid_levels:
            self._activity_level = level_lower

    @property
    def activity_level(self):
        return self._activity_level
    
    @property
    def daily_consumption(self):
        return self._daily_consumption
    
    def add_daily_consumption(self, food, quantity_grams, date):
        """Adiciona um alimento ao consumo diário do usuário."""
        consumption = DailyConsumption(food, quantity_grams, date)
        self._daily_consumption.append(consumption)

    def calculate_basal_metabolism(self):
        """Calcula o metabolismo basal usando a fórmula de Harris-Benedict."""
        if self._gender == "masculino":
            # Fórmula de Harris-Benedict para homens
            return 88.36 + (13.4 * self._weight) + (4.8 * self._height) - (5.7 * self._age)
        else:
            # Fórmula de Harris-Benedict para mulheres
            return 447.6 + (9.2 * self._weight) + (3.1 * self._height) - (4.3 * self._age)
    
    def calculate_total_energy_expenditure(self):
        """Calcula o gasto energético total (GET) ajustado pelo nível de atividade."""
        mb = self.calculate_basal_metabolism()

        activity_multipliers = {
            "sedentário": 1.2,
            "atividade leve": 1.375,
            "atividade moderada": 1.55,
            "atividade intensa": 1.725,
            "atividade muito intensa": 1.9
        }

        # Usa o multiplicador de atividade do primeiro nível de atividade
        activity_level = self._activity_level[0] if self._activity_level else "sedentário"
        multiplier = activity_multipliers.get(activity_level, 1.2)  # Default para "sedentário"
        
        return mb * multiplier

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "weight": self.weight,
            "height": self.height,
            "activity_level": self.activity_level,
            "goals": self.goals,
            "daily_consumption": [c.to_dict() for c in self._daily_consumption]
        }
    
    def __str__(self):
        name = f"{self.name}"
        age = f"{self.age}"
        gender = f"{self.gender}"
        weight = f"{self.weight}"
        height = f"{self.height}"
        activity_lvl = f"Nível de Atividade: {self._activity_level if self._activity_level else 'Nenhum'}"
        goals = f"Meta: {self._goals if self._goals else 'Nenhuma'}"

        return f"{name}\nIdade: {age}\nGênero: {gender}\nPeso: {weight}\nAltura: {height}\n{activity_lvl}\n{goals}"
