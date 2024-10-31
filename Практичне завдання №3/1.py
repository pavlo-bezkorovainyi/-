#  1
# Словники Python можуть використовуватися для моделювання «справжнього» словника (назвемо
# його глосарієм). Оберіть кілька термінів з програмування (або із іншої області), які ви знаєте на цей
# момент. Використайте ці слова як ключі глосарію, а їх визначення - як значення. Виведіть кожне
# слово і його визначення у спеціально відформатованому вигляді. Наприклад, ви можете вивести
# слово, потім двокрапка і визначення; або ж слово в одному рядку, а його визначення - з відступом в
# наступному рядку. Використовуйте символ нового рядка (\n) для вставки порожніх рядків між
# парами «слово: визначення» і символ табуляції для встановлення відступів (\t) у вихідних даних.


glossary = {
    "Variable": "A symbol or container that holds a value.",
    "Function": "A block of reusable code that performs a specific task.",
    "Loop": "A sequence of instructions that repeats until a condition is met.",
    "Dictionary": "A collection of key-value pairs.",
    "List": "An ordered collection of items."
}

for word, definition in glossary.items():
    print(f"{word}:\n\t{definition}\n")


