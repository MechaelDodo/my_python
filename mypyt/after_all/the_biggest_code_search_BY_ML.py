import os, pprint

dirname = r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt'
array_finally = []

for (thisDir, subFiles, otherFiles) in os.walk(dirname):
    for filename in otherFiles:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            array_finally.append((fullsize, fullname))

array_finally.sort()
pprint.pprint(array_finally[-2:])
            
