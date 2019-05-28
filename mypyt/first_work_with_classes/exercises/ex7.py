class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):
        print('order is %s' % (foodName))
        self.customer.placeOrder(foodName, self.employee)
    def result(self):
        self.customer.printOrder(self.employee)

class Customer:
    def __init__(self):
        self.food = None
    def placeOrder(self, foodName, employee):
        print('\tplace Order')
        employee.takeOrder(foodName)
    def printOrder(self, employee):
        print(employee.getNameFood())
    

class Employee:
    def takeOrder(self, foodName):
        print('\t\ttake Order')
        self.food = Food(foodName)
    def getNameFood(self):
        return self.food.name

class Food:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    lunch = Lunch()
    lunch.order('burger')
    lunch.result()
