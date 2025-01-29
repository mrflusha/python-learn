'''
Пусть дан следующий список, которые хранит несколько словарей:
1

    
people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

Каждый словарь в списке представляет программиста, где поле "name" представляет имя, а поле "languages" - список используемых языков программирования. 
Выведите на консоль из каждого словаря имя и последний язык программирования, чтобы получился следуюший консольный вывод:
'''


people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

for man in people:
    print(f"Name: {man['name']}\nLast language: {man['languages'][-1]}")