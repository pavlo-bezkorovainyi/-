# Завдання 4

digits_str = input("Введіть 5 цифр, розділених пропусками: ")

digits = digits_str.split()

reversed_digits = digits[::-1]

reversed_number = "".join(reversed_digits)

print("Число зі зворотним порядком:", reversed_number)