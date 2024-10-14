# Програма 1 (Завдання 6)
# Автор: Павло Безкорований
# Дата: 2024-10-14
# Програма для перетворення одиниць вимірювання відстаніpython distance_converter.py

distance_meters = float(input("Введіть відстань у метрах: "))

print("Відстань у метрах: {:.2f} м".format(distance_meters))
print("Відстань у дюймах: {:.2f} дюймів".format(distance_meters * 39.3701))
print("Відстань у футах: {:.2f} футів".format(distance_meters * 3.28084))
print("Відстань у ярдах: {:.2f} ярдів".format(distance_meters * 1.09361))
print("Відстань у милях: {:.2f} миль".format(distance_meters * 0.000621371))

