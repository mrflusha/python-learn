'''
Напишите программу, которая с помощью цикла создает список чисел от 1 до 10, а также списки их квадратов и кубов. В конце списки выводятся на консоль. Пример работы:

numbers:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
cubes :  [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

'''

numbers = list()
squares = list()
cubes = list()

for i in range(1,11): 
	numbers.append(i)
	squares.append(i ** 2)
	cubes.append(i ** 3)


print(f"numbers: {numbers}", f"squares: {squares}",f"cubes: {cubes}", sep = "\n")

