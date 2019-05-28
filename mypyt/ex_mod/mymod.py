import copy

def countLines(name):
    f = open(name)
    return len(f.readlines())

def countChars(name):
    return len(open(name).read())
    

def test(name):    
    return countLines(name), countChars(name)
    

if __name__ == '__main__':
    print(test('mymod.py'))
    
    
    
