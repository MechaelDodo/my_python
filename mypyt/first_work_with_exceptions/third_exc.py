def safe(func, *args):
    try:
        func(*args)
    except:
        import traceback, sys
        traceback.print_exc()       
        print('you have an error:', sys.exc_info()[0], sys.exc_info()[1])
        

def fun(s):
    print(s.upper())
if __name__ == '__main__':
    from first_exc import poo
    safe(poo)
    safe(fun, 'hello my friend!')
