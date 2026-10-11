import random
def generate_grades(count):
    return [random.randint(1, 12) for _ in range(count)]
def average_grade(grades):
    return sum(grades) / len(grades) if grades else 0
def get_level(average):
    if average >= 10:
        return "Високий"
    elif average >= 7:
        return "Достатній"
    elif average >= 4:
        return "Середній"
    else:
        return "Початковий"