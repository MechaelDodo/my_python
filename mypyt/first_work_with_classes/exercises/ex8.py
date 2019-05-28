class Animal:
    def speak(self):
        print('AAA')
    def reply(self):
        self.speak()

class Mammal(Animal):
    def speak(self):
        print('GAGA')

class Cat(Mammal):
    def speak(self):
        print('Meow')

class Dog(Mammal):
    def speak(self):
        print('Row')

class Primate(Mammal):
    def speak(self):
        print('Hello world!')

class Hacker(Primate):
    pass
    #def speak(self):
        #print('Python eee')

if __name__ == '__main__':
    a = Hacker()
    a.reply()
