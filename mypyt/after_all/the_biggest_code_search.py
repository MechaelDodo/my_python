import os, glob, pprint

dirname = r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt'

list_files = glob.glob(dirname + os.sep + '*.py')
array_f = [] 

for filename in list_files:
    with open(filename) as file:
        array_f.append((len(file.read()), filename))

array_f.sort()
print(array_f)
print('The biggest code: ', array_f[len(array_f) - 1],'\n\n\n')
pprint.pprint(array_f[-1:])
