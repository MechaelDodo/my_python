#import mymod
#print(mymod.countLines(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\ex_mod\test.txt'))
#print(mymod.countChars(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\ex_mod\test.txt'))
#print(mymod.test(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\ex_mod\test.txt'))

from mymod import *

print(countLines(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\ex_mod\test.txt'))
print(countChars(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\ex_mod\test.txt'))
print(test(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\ex_mod\test.txt'))
