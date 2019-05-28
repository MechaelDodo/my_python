"""
this is my example for txts file
"""

fr=open('C://Users//admin//AppData//Local//Programs//Python//Python37-32//mypyt//txtF//hahaFirst.txt','r')
fw=open('C://Users//admin//AppData//Local//Programs//Python//Python37-32//mypyt//txtF//hahaFirst.txt','w')

fw.write('one sad\n')
fw.write('two sad\n')
fw.close()

mystr1=fr.readline()
mystr2=fr.readline()
mystr3=fr.readline()
mystr4=fr.readline()
#fr.close()

print('..1..'+mystr1+'..2..'+mystr2+'..3..'+mystr3+'..4..'+mystr4)

"""
this is my example for bins file
"""

fr=open('C://Users//admin//AppData//Local//Programs//Python//Python37-32//mypyt//txtF//myBinFile.bin','rb')

#fw=open('C://Users//admin//AppData//Local//Programs//Python//Python37-32//mypyt//txtF//myBinFile.bin','wb')

#fw.write('\x00\x00\x00\x07spam1\x00\x08')
#fw.write('\x00\x00\x00\x07spam2\x00\x08')
#fw.close()

mystr1=fr.read()

#fr.close()

print(mystr1)

"""
this is my example for file with modul "pickle"
"""

sL = {'ass':123,'haha':'lala','ww':47}

fr=open('C://Users//admin//AppData//Local//Programs//Python//Python37-32//mypyt//txtF//hahaFirst.txt','rb')
fw=open('C://Users//admin//AppData//Local//Programs//Python//Python37-32//mypyt//txtF//hahaFirst.txt','wb')

import pickle
pickle.dump(sL,fw)
fw.close()

secondSL = pickle.load(fr)
print(secondSL['ass'])

def helloW():
    """
    This function puts some words in out
    """
    print('hello world')


