# Создать класс Person у которого есть свойство класса Wallet (кошелек).
# Создать класс Pay с методом оплаты с аргументом объекта Person и суммой покупки. 
# При недостаточном количестве средств в кошельке его значение не меняется и выводится соответствующее сообщение.
# Если средств достаточно, то эта сумма списывается с кошелька пользователя 


class Person:
    def __init__(self,wallet=''):
        self.__wallet = wallet

    

class Wallet:    
    @property 
    def wallet(self):
        return self.__wallet

    @wallet.setter
    def wallet(self,value):
       self.__wallet = value



class Pay:
    wallet = Person()
    def __init__(self,money_count):
        self.money_count = money_count

    def pay(self):
        if self.wallet >= self.money_count:
            return self.wallet-self.money_count
        else:
            print("Не хватает денег")


p1 = Pay(1001)
p1.wallet = 2012
print(p1.pay())




# p1 = Person(1010)
# p2 = Wallet(1000)
# p3 = Pay(120)
# print(p2.wallet)
# p1.wallet = 100
# print(p1.wallet)
