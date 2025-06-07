# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
# представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.


class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def print_info(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")


# Створюємо об'єкт студента
student = Student("Олександр", "Романченко", 21, 88.5)

# Виводимо інформацію
print("До зміни балу:")
student.print_info()

# Оновлюємо середній бал
student.update_average_grade(92.3)

# Виводимо оновлену інформацію
print("\nПісля зміни балу:")
student.print_info()
