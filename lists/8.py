'''
Напишите функцию, которая принимает два списка и возвращает новый список, в котором каждый элемент представляет сумму соответствующих элементов обоих списков. 
'''


def add(fst_lst, scnd_lst):
	third_lst = list()
	for i, j in zip(fst_lst, scnd_lst):
		third_lst.append(i + j)
		print(i,j )
	return third_lst


