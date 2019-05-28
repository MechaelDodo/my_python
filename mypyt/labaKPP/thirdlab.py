class Money:

    "This class has got a name of owner and amount of money"

    def __init__(self, amount, owner):
        self.amount = amount
        self.owner = owner



class client:
    
    "This is class is a parent for others classes"
    
    def __init__(self, name):
        self.name = name

    def give_money(self, inPas, logIn):       ###
        global atm,richClient,studentClient,poorClient
        reqPas = atm.passwordRequest(inPas)
            
        if reqPas == 'Ok':
            if logIn == richClient.login:
                countOfMoney = input('Введите сумму денег, которую хотите снять')
                atm.giveBanksMoney(countOfMoney)
                richClient.money += countOfMoney
            elif logIn == studentClient.login:
                countOfMoney = input('Введите сумму денег, которую хотите снять')
                atm.giveBanksMoney(countOfMoney)
                studentClient.money += countOfMoney
            elif logIn == poorClient.login:
                countOfMoney = input('Введите сумму денег, которую хотите снять')
                atm.giveBanksMoney(countOfMoney)
                poorClient.money += countOfMoney
           
        pass

class RichCl(client):

    "This is class for the rich client"

    def __init__(self, name = ''):
        self.name = name
        self.login = 'logR'
        self.password = 'rich'
        self.money = 10000

class Student(client):

    "This is class for student"

    def __init__(self, name = ''):
        self.name = name
        self.login = 'logS'
        self.password = 'stud'
        self.money = 50

class poorCl(client):

    "This is class for the poor client"

    def __init__(self, name = ''):
        self.name = name
        self.login = 'logP'
        self.password = 'poor'
        self.money = 0


class ATM:                                  ###

    "This class has got a name of the bank and amount of banks money" 

    def __init__(self):
        global richClient, studentClient, poorClient
        self.bank = 'MTBank'
        self.bankMoney = 5000000
        self.allPasswords = {richClient.name:'rich', studentClient.name:'stud',
                             poorClient.name:'poor'}
    
    def giveBanksMoney(self,count):
        self.bankMoney-=count
        return count

    def passwordRequest(self, inPassword):  ###
        global richClient,studentClient,poorClient
        if (self.allPassords[richClient.name] == inPassword |
            self.allPassords[studentClient.name] == inPassword |
            self.allPassords[poorClient.name] == inPassword):
            return 'Ok'
           
atm = ATM()

if __name__ == '__main__':
    
    while True:
        logIn = input('Введите ваш логин: ')
        if logIn == 'logR':
            nameOf = input('Введите ваше имя: ')
            richClient = RichCl(nameOf)
            while True:
                moneyOfATM = input('Введите сумму,которую хотите взять: ')
                password = input('Введите пароль: ')          
                richClient.give_money(password, moneyOfATM)
        elif logIn == 'logS':                                       ###                           
                nameOf = input('Введите ваше имя: ')
                studentClient = Student(nameOf)
        elif logIn == 'logP':                                       ###            
                nameOf = input('Введите ваше имя: ')
                poorClient = poorCl(nameOf)
        else:
            print('Такого логина не существует...')


           










