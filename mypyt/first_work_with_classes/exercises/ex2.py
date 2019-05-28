class MyList:
    def __init__(self, arr = []):
        self.arr = []
        for i in arr:
            self.arr.append(i)
    def __str__(self):
        return 'my list: %s' % self.arr
    def __getattr__(self, attr):
        return getattr(self.arr, attr)
    def __add__(self, other):
        return MyList(self.arr + other)
    def __getitem__(self, item):
        return self.arr[item]
    def __iter__(self):
        self.start = -1
        self.stop = len(self.arr) - 1
        return self
    def __next__(self):
        if self.start == self.stop:
            del self.start; del self.stop
            raise StopIteration
        self.start += 1
        return self.arr[self.start]

if __name__ == '__main__':
    b = MyList([121, 23, 312, 45])
    a = MyList(b)
    a.append(20)
    a.sort()
    for i in a:
        print(i)
