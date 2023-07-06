from typing import Iterable

class Student:
    BASE_SCOHALARSHIP = 17000
    
    def __init__(self, 
                 name: str, 
                 age: int, 
                 grades: Iterable[int]
            ):
        self.name = name
        self.age = age
        self.grades = list(grades)
        
    def calculate_schoralship(self) -> float:
        return round(((sum(self.grades) / len(self.grades) - 2) / 3) * self.BASE_SCOHALARSHIP)
    
    def add_grade(self, grade: int):
        self.grades.append(grade)
        
    def clear_grades(self):
        self.grades.clear()
        
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, self.__class__):
            raise NotImplemented
        else:
            return self.name == __value.name
    
    def __repr__(self) -> str:
        return f'Student(name={self.name}, age={self.age}, grades={self.grades})'

    def __str__(self) -> str:
        return f'{self.name}, {self.age}, {self.grades}'
ruslan = Student("Ruslan", 19, [5, 4, 4, 4, 5])

print(ruslan.calculate_schoralship())
print(ruslan == object())

