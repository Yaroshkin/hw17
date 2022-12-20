# Создать класс Person у которого есть свойство класса Wallet (кошелек).
# Создать класс Pay с методом оплаты с аргументом объекта Person и суммой покупки. 
# При недостаточном количестве средств в кошельке его значение не меняется и выводится соответствующее сообщение.
# Если средств достаточно, то эта сумма списывается с кошелька пользователя 


class Person:
    def __init__(self,money):
        self.money = money

    @property 
    def Wallet(self):
        if  self.money < self.money_count

class Pay:
    def __init__(self,money_count) -> None:
        self.money_count = money_count

    def pay(self):
        pass