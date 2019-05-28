from ex2 import MyList

class MyListSub(MyList):
    calls = 0
    def __init__(self, arr):
        MyList.__init__(self, arr)
    def __add__(self, ar):
        MyListSub.calls += 1
        print('add:', MyListSub.calls)
        return MyList.__add__(self, ar)

if __name__ == '__main__':
    b = MyList([121, 23, 312, 45])
    a = MyListSub(b)
    a.append(20)
    a.sort()
    for i in a:
        print(i)
    b = a + [1, 2, 3]
    
    print(b)
    c = a + [22, 33, 44]
    print(c.__class__)
