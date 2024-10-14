number = int(input("Введіть чотирицифрове число: "))

digits = [int(digit) for digit in str(number)]
sum_of_digits = sum(digits)

print(f"{' + '.join(map(str, digits))} = {sum_of_digits}")
