# Завдання 2

numbers_str = input("Введіть числа, розділені пропусками: ")

numbers = list(map(int, numbers_str.split()))

sum_of_numbers = sum(numbers)

print("Сума чисел:", sum_of_numbers)