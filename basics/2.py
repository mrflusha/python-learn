'''
Напишите программу, в которой пользователь вводит температуру в градусах Цельсия, а программа переводит их в градусы Фаренге́йта. Для перевода применяется формула:
	
°F= (9/5)*(°C) + 32
'''


degres_c = float( input("Введите температуру в градусах цельсия: ") )

degres_f = ( 9 / 5 ) * degres_c + 32 

print(f"{degres_f}")

