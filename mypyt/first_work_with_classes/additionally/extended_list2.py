class Set(list):
    def __getitem__(self, item):
        return list.__getitem__(self, item - 1)

if __name__ == '__main__':
    arr = Set([1, 2, 3, 4, 5])
    print(arr[2])
