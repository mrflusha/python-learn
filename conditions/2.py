'''
Напишите программу, в которую пользователь вводит два числа, а программа выводит сообщение, какое из чисел наибольшее. 
'''

a = int(input("Enter A:"))
b = int(input("Enter B:"))



def match(a , b):
	return a > b

result = match(a,b)

if result:
	print(f"Наибольшее число: {a}")
else:
	print(f"Наибольшее число: {b}")
