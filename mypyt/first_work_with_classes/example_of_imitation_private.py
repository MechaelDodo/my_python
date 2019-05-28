"""
exeample of imitation of private atributes
"""
class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value
    def __getattr__(self, attrname):
        if attrname in privates:
            raise AttributeError
        elif attrname == 'old':
            return 'fuck'

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

class Human(Exception):
    privates = ['politics','old']
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value
    def __getattr__(self, attrname):
        if attrname in privates:
            raise AttributeError
        elif attrname == 'old':
            return 'fuck'
 
    def __init__(self, name, old, job, gender):
        self.name = name
        self.__dict__['old'] = old
        self.job = job
        self.gender = gender
        
    

if __name__ == '__main__':
    woman = Human('Masha', 20, 'cashier', 'female')
    print(woman.old)
            
    
