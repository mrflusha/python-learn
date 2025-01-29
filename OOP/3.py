'''
Создайте класс Vector, который представляет вектор и определите в нем операторы сложения и вычитания. Для сложения векторо применяется формула a + b = {ax + bx; ay + by}, а для вычитания a - b = {ax - bx; ay - by}
'''

class Vector:
	def __init__ (self, a , b):
		self.__a = a
		self.__b = b

	def __add__ (self, other):
		return Vector(self.__a + other.__b, other.__a + self.__b)
	def __sub__ (self, other):
		return Vector(self.__a - other.__b, other.__a - self.__b)


	def print_vector(self):
		print(self.__a, self.__b)


vector1 = Vector(2,5)

vector2 = Vector(3,7)

vector3 = vector2 + vector1
vector4 = vector1 - vector2

vector4.print_vector()
