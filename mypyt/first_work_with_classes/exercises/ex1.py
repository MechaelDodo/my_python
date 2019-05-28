from copy import copy

class Adder:
    def __init__(self, data = []):
        self.data = data
    def add(self, y):
        raise NotImplementedError('Function Is Not Implemented')
    def __add__(self, other):
        return self.add(other)
    
class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        z = copy(self.data)
        for key in list(y.keys()):
            z[key] = y[key]
        return z

if __name__ == '__main__':
    a = DictAdder({'s': 11, 'sad': 42})
    print(a + {'dad':'wer'})
    b = ListAdder([1, 2, 3])
    print(b + [4, 5, 6, 7])
    print(a.data)
