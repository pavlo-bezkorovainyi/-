# 3. Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов
# (значення). Виведіть по черзі для усіх елементів словника повідомлення типу My favorite
# programming language is Python. It was created by Guido van Rossum.. Видаліть,
# на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(f"My favorite programming language is {language}. It was created by {creator}.")

del languages["JavaScript"]

print("\nUpdated dictionary:")
for language, creator in languages.items():
    print(f"{language}: {creator}")