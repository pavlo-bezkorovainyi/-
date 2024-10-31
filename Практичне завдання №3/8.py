# 8. Створіть словник з ім’ям cities. Використайте назви трьох міст в якості ключів словника.
# Створіть словник з інформацією про кожне місто: включіть в нього країну, в якій розташоване
# місто, приблизну чисельність населення і один цікавий факт про місто. Ключі словника кожного
# міста повинні називатися country, population і fact. Виведіть назву кожного міста і всю
# збережену інформацію про нього.

# Створюємо словник з інформацією про міста
cities = {
    "Kyiv": {
        "country": "Ukraine",
        "population": "2.8 million",
        "fact": "Kyiv is one of the oldest cities in Eastern Europe."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "37 million",
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "New York": {
        "country": "USA",
        "population": "8.3 million",
        "fact": "New York is known as the 'Big Apple'."
    }
}

# Виводимо інформацію про кожне місто
for city, info in cities.items():
    print(f"\nМісто: {city}")
    print(f"Країна: {info['country']}")
    print(f"Населення: {info['population']}")
    print(f"Цікавий факт: {info['fact']}")
