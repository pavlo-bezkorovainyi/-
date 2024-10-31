# 5. Створіть кілька словників, імена яких - це клички домашніх тварин. У кожному словнику збережіть
# інформацію про вид домашнього улюбленця та ім’я власника. Збережіть словники в списку з ім’ям
# pets. Виведіть кілька повідомлень типу Alex is the owner of a pet - a dog..

# Створюємо словники для домашніх тварин з інформацією про вид тварини та ім'я власника
pet1 = {
    "name": "Alex",
    "type": "dog",
    "owner": "John"
}

pet2 = {
    "name": "Milo",
    "type": "cat",
    "owner": "Sarah"
}

pet3 = {
    "name": "Goldie",
    "type": "fish",
    "owner": "Mike"
}

# Зберігаємо словники у списку
pets = [pet1, pet2, pet3]

# Виводимо інформацію про кожну тварину
for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - {pet['type']} named {pet['name']}.")