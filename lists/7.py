'''

Напишите программу, которая удаляет из списка чисел четные числа. 

'''

array = [11, 22, 33, 44, 55]


for number in array:
	if number % 2 == 0:
		array.remove(number)

