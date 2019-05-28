from person import *
import pickle

man1 = Manager('Mechael Dodo', 20000)
man2 = Person('Joji')
file = open(r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\first_work_with_classes\dodo.pkl','wb')
arr = [man1, man2]
pickle.dump(arr, file)
file.close()


man3 = Person('Stepan Veteran', 'dancer', 7000)
import shelve
db = shelve.open('personshelvedb')
for obj in (man1, man2, man3):
    db[obj.name] = obj
db.close()

import glob
print(glob.glob('pers*'))
