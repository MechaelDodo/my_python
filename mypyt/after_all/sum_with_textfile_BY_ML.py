import os

dirname = r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\after_all'
text_file_name = 'test_sum.txt'
dictfinally = {}

for line in open(os.path.join(dirname, text_file_name)):
    line = [int(num) for num in line.split(',')]
    for (index, num) in enumerate(line):
        dictfinally[index] = dictfinally.get(index, 0) + num

print(dictfinally)
    
