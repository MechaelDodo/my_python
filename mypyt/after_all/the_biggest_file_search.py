import os, glob

dirname = r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt'
list_names_py = glob.glob(dirname + os.sep + '*.py')
array_finally = []

for filename in list_names_py:
    filename_zise = os.path.getsize(filename)
    array_finally.append((filename_zise, filename))


array_finally.sort()
print(array_finally)
print('The biggest file:', array_finally[len(array_finally)-1])

