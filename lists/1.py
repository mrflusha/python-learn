'''
Создайте список из имен-строк. Затем добавьте в этот список два новых имени и удалите последнее имя. Выведите финальный список на консоль.
'''


names = ["Alice", "Jay", "Bob"]


names.append("Vasyliy")
names.append("Petr")

names.pop(-1)

print(names)

