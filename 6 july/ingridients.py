class Ingridient:
    def __init__(self, calories: float, mass: float) -> None:
        self._calories = calories
        self._mass = mass
        
    def prepare(self) -> float:
        """Подготавливает еду к употреблению"""
        return self._calories
    
    def get_calories(self) -> float:
        """Возращает калории"""
        return self._calories
    def get_mass(self) -> float:
        """Возвращает массу"""
        return self._mass
    
