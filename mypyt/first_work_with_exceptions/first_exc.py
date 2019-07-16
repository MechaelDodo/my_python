class MyError(Exception):   pass

def oops():
    raise MyError

def poo():
    try:
        oops()
    except (IndexError, KeyError, MyError) as E:
        print('OK', E.__class__.__name__)

if __name__ == '__main__':
    poo()
