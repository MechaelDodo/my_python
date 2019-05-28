import pickle 
import sys
sys.path.append(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\best_modules')
import classtools #type: ignore
import test_instance.lister

def writePickle(objectsList):
    """
    this function loads objects from list to the <picklefile 'datafile.pkl'>
    """
    file = open('datafile.pkl','wb')
    pickle.dump(objectsList, file)
    file.close()

def readPickle():
    """
    this function returns list from <picklefile 'datafile.pkl'>
    """
    file = open('datafile.pkl','rb')
    return pickle.load(file)

    

class Person(test_instance.lister.ListInstance):
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, a_raise):
        self.pay = int(self.pay + self.pay*a_raise)

class Manager(Person):
    old = 20
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)
    def giveRaise(self, a_raise, a_managers_bonus = 0.1):
        Person.giveRaise(self, a_raise + a_managers_bonus)

class Manager_secondVersion(classtools.AttrDisplay):
    def __init__(self, name, pay):
        self.person = Person(name, 'Manager (second version class)', pay)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def giveRaise(self, a_raise, a_managers_bonus = 0.05):
        self.person.giveRaise(a_raise + a_managers_bonus)

class Department:
    def __init__(self, *args):
        self.members = list(args)        
    def __contains__(self, obj):
        print('contains: ',end = '')
        return obj in self.members
    def __iter__(self):
        self.start = -1
        self.stop = len(self.members) - 1
        print('iter => ', end = '')
        return self    #
    def __next__(self):
        print('next: ', end = '')
        if self.start == self.stop:
            #self.start = -1
            del self.start
            del self.stop
            print('--Stop iteration!--') 
            raise StopIteration
        self.start += 1
        return self.members[self.start]
    def __getitem__(self, index):
        return self.members[index]
    def __setitem__(self, index, obj):
        self.members[index] = obj
    def showAll(self):
        for obj in self.members:    
            print('Last Name:', obj.lastName())
            print(obj, end = '\n---\n')
    def addMember(self, obj):
        self.members.append(obj)
        self.stop += 1
    def giveRaise(self, a_raise):
        for obj in self.members:
            obj.giveRaise(a_raise)
    def loadAll(self):
        """
        method 'loadAll' does not work well
        with <class 'person.Manager_secondVersion'>.
        It load the object, but it does not reload it.
        """
        writePickle(self.members)   
                                    
def poo(s: str):
	return s*2
        

    
if __name__ == '__main__':        
    
    p1 = Manager('Misha Odod', 10000)
    p2 = Person('Danya Virh', job = 'BI', pay = 10000)
    p3 = Person('Joj')
    p4 = Manager_secondVersion('Stas Bruilo', 10000)
            
    print(p1)
    print('----------------')
    dep1 = Department(p1, p2, p3)
    #dep.addMember(p4)
    dep1.giveRaise(0.1)
    dep1.showAll()

    dep1.loadAll()    
    dep2 = Department(*readPickle())
    dep2.showAll()

    print(poo('sad'))
    print(poo(3))
    print(poo('la'))
    print(poo(6))

    dep2[2] = Person('sad man')
    print(dep2[2], end = '\n___\n')
    for obj in dep2:
        print('1)', obj)
    print()
    for obj in dep2:
        print('2)', obj)
    I1 = iter(dep2)
    I2 = iter(dep2)
    print(next(I1))
    print(next(I2))
    print(next(I1))
    print(next(I2))

    




 

    
        
