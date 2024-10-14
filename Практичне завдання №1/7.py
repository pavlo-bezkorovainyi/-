days = 10
hours = days * 24

days = int(input("Введіть кількість днів: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Години: {hours:<10}")
print(f"Хвилини: {minutes:<10}")
print(f"Секунди: {seconds:<10}")