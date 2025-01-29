'''
Определите класс Rectangle, который представляет прямоугольник. Через конструктор класс принимает ширину и длину и сохраняет их в атрибутах width и length соответственно. Также этом классе определите метод area, который возвращает площадь прямоугольника, и метод perimeter, который возвращает периметра прямоугольника.

После создания класса определите несколько объектов класса Rectangle и продемонстрируйте работу его методов.
'''

class Rectangle:
	def __init__ (self, width, length):
		self.width = width
		self.length = length

	def area (self):
		return self.width * self.length

	def perimeter(self):
		return 2 * (self.width + self.length)




a = Rectangle(2,5)

print(f"Площадь: {a.area()} \nПериметр:{a.perimeter()}")