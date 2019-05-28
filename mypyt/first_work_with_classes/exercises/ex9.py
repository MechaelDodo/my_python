class Scene:
    def __init__(self):
        self.cust = Customer()
        self.clerk = Clerk()
        self.par = Parrot()
    def action(self):
        for cl in (self.cust, self.clerk, self.par):
            print('%s: ' % cl.__class__.__name__, end = '')
            cl.line()

    

class Customer:
    def line(self):
        print('hello world!')

class Clerk:
    def line(self):
        print('I am clerk!')

class Parrot:
    def line(self):
        print('Popka is fool!')

if __name__ == '__main__':
    Scene().action()
