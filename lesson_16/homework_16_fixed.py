from abc import ABC, abstractmethod
import math

# -----------------------------
# Завдання 1: Ієрархія класів
# -----------------------------


class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size


# Тест для перевірки атрибутів
lead = TeamLead(
    name="Anna",
    salary=3500,
    department="Engineering",
    programming_language="Python",
    team_size=5,
)

print("\n Перевірка TeamLead:")
print("Ім'я:", lead.name)
print("Зарплата:", lead.salary)
print("Відділ:", lead.department)
print("Мова програмування:", lead.programming_language)
print("Розмір команди:", lead.team_size)

# -----------------------------
#  Завдання 2: Абстрактний клас Figure
# -----------------------------


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius**2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side**2

    def perimeter(self):
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


# Тест фігур
print("\nПеревірка фігур:")
figures = [Circle(5), Square(4), Rectangle(3, 6)]

for fig in figures:
    print(
        f"{fig.__class__.__name__}: Площа = {fig.area():.2f}, Периметр = {fig.perimeter():.2f}"
    )
