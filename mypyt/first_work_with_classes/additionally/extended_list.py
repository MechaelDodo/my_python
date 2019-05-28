import copy
class Set(list):
    def __init__(self, value = []):
        list.__init__([])
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in other:
            if x in self:
                res.append(x)
        return Set(res)
    def union(self, other):
        res = copy.copy(self)
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)
    def concat(self, value):
        for x in value:
            if x not in self:
                self.append(x)
    def __str__(self):
        return 'My array "%s": %s' % (self.__class__.__name__, list.__str__(self))  #!!! list.__str__(self)
    def __len__(self):              return len(self)
    def __getitem__(self, item):    return self[item]
    def __and__(self, other):       return self.intersect(other)
    def __or__(self, other):        return self.union(other)
    

if __name__ == '__main__':
    arr = Set([1, 2, 2, 3, 4, 5])
    print(arr)
    a = [4, 5, 6, 7, 8]
    print(arr.intersect(a))
    print(arr & a)
    print(arr.union(a))
    print(arr | a)
