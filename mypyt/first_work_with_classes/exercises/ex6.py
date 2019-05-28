from mypyt.first_work_with_classes.test_instance.lister import ListInstance

class A(ListInstance):          pass
class B(A):                     pass
class C(A):                     pass
class D(B, C):                  pass
class E:                        pass
class F(D,E):                   pass

if __name__ == '__main__':
    d = D()
    print(d)
