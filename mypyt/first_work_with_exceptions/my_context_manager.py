class Tr:
    def __init__(self, file):
        self.file = file
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        if exc_type is None:
            print(' OK ')
        else:
            print('error lol')
            return False

if __name__ == '__main__':
    with Tr(open('test.txt')) as t:
        for line in t.file:
            print(line, end = '')
