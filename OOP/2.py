'''
Создайте класс BankAccount, который представляет банковский счет. Определите в этом классе атрибуты account_number и balance, которые представляют номер счета и баланс. Через параметры конструктора передайте этим атрибутам начальные значения.

Также в классе определите метод add, который принимает некоторую сумму и добавляет ее на баланс счета. И определите метод withdraw, который принимает некоторую сумму и снимает ее с баланса. При этом с баланса нельзя снять больше, чем имеется. Если на балансе недостаточно средств, то пользователю должно выводиться соответствующее сообщение.
'''



class BankAccount:
	def __init__ (self, account_number:int, balance:float):
		self.account_number = account_number
		self.balance = balance

	def add (self, sum):
		self.balance += sum

	def withdraw (self, sum):
		if sum <= self.balance:
			self.balance -= sum
		else:
			print("NO MONEY")



money = BankAccount(2,2.5)


money.add(500)

print(money.balance)

money.withdraw(30)
print(money.balance)

money.withdraw(1000)