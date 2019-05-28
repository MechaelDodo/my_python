def adder1(*args):
    arg=args[0]
    for i in args[1:]:
        arg+=i
    return arg

def adder2(**args):
    keyargs=list(args.keys())
    arg=args[keyargs[0]]
    for i in keyargs[1:]:
        arg+=args[i]
    return arg

#print(adder2(a=1,b=2,c=3))
import copy
def copyDict(dic):
    newdic={}
    for i in dic:
        newdic[i]=dic[i]
    return newdic

dic1={'sad1':1231,'haha1':'lol1'}
dic2={'sad2':1232,'haha1':'lol2'}

#print(copyDict(dic))

def addDict(dict1,dict2):
    if type(dict1)==list or type(dict2)==list:
        return 'You send list. Please use dict' 
    newdic={}
    for i in dict1:
        newdic[i]=dict1[i]
    for i in dict2:
        newdic[i]=dict2[i]
    return newdic
list1=[1,2,3]
list2=[4,5,6]
#print(addDict(dic1,dic2))
#print(addDict(list1,list2))

def f1(a,b):print(a,b)
def f2(a,*b):print(a,b)
def f3(a,**b):print(a,b)
def f4(a,*b,**c):print(a,b,c)
def f5(a,b=2,c=3):print(a,b,c)
def f6(a,b=2,*c):print(a,b,c)

def primefun(x):
    y=x//2
    while y>1:
        if x%y==0:
            print(x,'has factor',y)
            break
        y-=1
    else:
        print(x,'is prime')

    
