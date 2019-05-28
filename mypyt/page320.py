f=open(r'E:\ucheba\myfile.txt','w')
myString='Hello file world!'
f.write(myString)
f.close()
f=open(r'E:\ucheba\myfile.txt')
myString=f.read()
print(myString)

