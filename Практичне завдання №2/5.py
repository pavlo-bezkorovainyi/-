# Завдання 5

professions = ["Doctor", "Engineer", "Teacher", "Nurse", "Artist"]

professions.append("Lawyer")
print("Після append():", professions)

professions.insert(2, "Architect")
print("Після insert():", professions)

professions.remove("Nurse")
print("Після remove():", professions)

popped_profession = professions.pop()
print("Після pop():", professions)
print("Видалений елемент:", popped_profession)

professions.sort()
print("Після sort():", professions)

professions.reverse()
print("Після reverse():", professions)

length = len(professions)
print("Довжина списку:", length)

index = professions.index("Doctor")
print("Індекс 'Doctor':", index)

count = professions.count("Engineer")
print("Кількість 'Engineer':", count)

professions.clear()
print("Після clear():", professions)